from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import uic, QtCore
from scipy import signal
from scipy.io import wavfile
import scipy.fftpack as ff
from goprocam import GoProCamera, constants
from views.SelectGoproFile import SelectGoproFile
from bs4 import BeautifulSoup
from itertools import combinations
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2
import math
import requests
import os


MergeDataWidgetPath = os.path.dirname(os.path.realpath(__file__)) + '\\MergeDataWidget.ui'
Ui_MergeDataWidget, QtBaseClass = uic.loadUiType(MergeDataWidgetPath)


class MergeDataWidget(QWidget, Ui_MergeDataWidget):
    def __init__(self):
        super(MergeDataWidget, self).__init__()

        self.setupUi(self)
        self.connect_button()

        self.goproColormap = 'gray'
        self.noiseDataColormap = 'viridis'

        self.noiseDataPath = ''
        self.goproFrontImagePath = ''
        self.goproBackImagePath = ''
        self.finalImagePath = ''

        self.fromComputerButtonClicks = 0
        self.fromCameraButtonClicks = 0
        self.loadNoiseFileButtonClicks = 0
        self.mergeDataButtonClicks = 0

        self.t1 = 30
        self.t2 = 32
        self.f1 = 100
        self.f2 = 2000
        self.Ar = None
        self.Athe = None
        self.Aphi = None
        self.nbMic = None

        self.PB_mergeData.setEnabled(False)
        self.PB_saveAs.setEnabled(False)
        self.PB_fromCamera.setEnabled(False)
        self.SL_transparencyCmap.setEnabled(False)

    def connect_button(self):
        self.PB_fromComputer.clicked.connect(self.load_from_computer)
        self.PB_loadNoiseFile.clicked.connect(self.display_noise_data)
        self.PB_fromCamera.clicked.connect(self.load_from_gopro)
        self.PB_saveAs.clicked.connect(self.save_final_image)
        self.PB_mergeData.clicked.connect(self.merge_data)

    def load_from_computer(self):
        try:
            self.goproFrontImagePath = self.ask_open_filename('Choose front GoPro Image')
            self.display_image_to_label(self.LA_imageGoproFront, self.goproFrontImagePath, self.goproColormap)
            self.goproBackImagePath = self.goproFrontImagePath.replace('GPFR', 'GPBK')
            # self.goproBackImagePath = self.ask_open_filename('Choose back GoPro Image')
            self.display_image_to_label(self.LA_imageGoproBack, self.goproBackImagePath, self.goproColormap)
            self.fromComputerButtonClicks += 1
            self.enable_merge_mata_button()
        except TypeError:
            self.PB_fromCamera.setEnabled(True)

    def ask_open_filename(self, windowTitle):
        path = QFileDialog.getOpenFileName(self, windowTitle)
        return path[0]

    def load_from_gopro(self):
        try:
            self.get_gopro_content()
            print(self.goproFrontImagePath, self.goproBackImagePath)
            self.fromCameraButtonClicks += 1
            self.enable_merge_mata_button()
        except AttributeError:
            self.PB_fromCamera.setEnabled(False)
            self.load_from_computer()

    def get_online_gopro_file(self, url):
        ext = '.JPG'
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        return [node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

    def get_gopro_content(self):
        # gpCam = GoProCamera.GoPro(constants.auth)
        # cameraDir = gpCam.getMediaFusion()
        cameraDir = ['http://10.5.5.9/videos/DCIM/100GBACK/GPBK0010.JPG',
                     'http://10.5.5.9/videos2/DCIM/100GFRNT/GPFR0010.JPG']
        cameraDir[0] = cameraDir[0][0:37]
        cameraDir[1] = cameraDir[1][0:38]

        # cameraFile = []
        # for file in self.get_online_gopro_file(cameraDir[0]):
        #     cameraFile.append(cameraDir[0][0:15] + file)

        cameraFile = ['http://10.5.5.9/videos2/DCIM/100GFRNT/GPFR0006.JPG',
                      'http://10.5.5.9/videos2/DCIM/100GFRNT/GPFR0010.JPG']
        for i in range(len(cameraFile)):
            cameraFile[i] = cameraFile[i][-8:]

        self.selectGoproFile = SelectGoproFile(cameraFile)
        self.selectGoproFile.exec_()
        imageFileName = self.selectGoproFile.fileName

        front = 'GPFR' + imageFileName
        back = 'GPBK' + imageFileName
        self.goproFrontImagePath = cameraDir[1] + front
        self.goproBackImagePath = cameraDir[0] + back

    def display_noise_data(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        fs, sig = self.wav_file_open(script_dir)
        self.get_angle(fs, sig)
        self.noiseDataPath = script_dir[:-5] + 'noise_angle.png'
        self.noiseDataPath = self.noiseDataPath.replace(os.sep, '/')
        self.display_image_to_label(self.LA_noiseData, self.noiseDataPath, self.noiseDataColormap)
        self.loadNoiseFileButtonClicks += 1
        self.enable_merge_mata_button()

    def wav_file_open(self, script_dir):
        # Fonction tirée du script Beamforming3D de Soft dB
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', os.path.expanduser("~/Desktop"),
                                                         'Wave Files (*.wav)')

        if fname != '':
            fs, sig = wavfile.read(fname)
            Ls = np.size(sig, 0) / fs
            Time = np.arange(0, np.size(sig, 0), 1) / fs

            sens = pd.read_excel(os.path.join(script_dir, "Supplements/Sensibilite_microphones.xlsx"), header=None)
            sens = np.transpose(np.atleast_2d(sens.iloc[1:, 2].values.astype('float64')))
            sig = np.transpose(sig) * sens

            tmp = pd.read_excel(os.path.join(script_dir, "Supplements/Position_microphones.xlsx"), header=None)
            Scale_Up = tmp.iloc[0, 3]

            self.Aphi = tmp.iloc[3:, 3].values.astype('float64')
            self.Athe = tmp.iloc[3:, 4].values.astype('float64')
            self.Ar = Scale_Up * tmp.iloc[3:, 2].values.astype('float64')

            self.nbMic = len(self.Aphi)

            return fs, sig

    def get_angle(self, fs, sig):
        # Fonction tirée du script Beamforming3D de Soft dB
        Nfft = fs
        c0 = 343
        # Coordonnées de l'antenne en dregrés
        Ax = self.Ar * np.cos(np.deg2rad(self.Athe)) * np.cos(np.deg2rad(self.Aphi))
        Ay = self.Ar * np.cos(np.deg2rad(self.Athe)) * np.sin(np.deg2rad(self.Aphi))
        Az = self.Ar * np.sin(np.deg2rad(self.Athe))

        comb = np.array(list(combinations(np.arange(self.nbMic), 2)))

        # Scan zone
        phi = np.atleast_2d(np.arange(-180, 181, 1))
        the = np.atleast_2d(np.arange(-90, 91, 1))
        Nobs = np.size(phi, 1) * np.size(the, 1)

        gridx = np.reshape(np.transpose(np.cos(np.deg2rad(the))) * np.cos(np.deg2rad(phi)), Nobs)
        gridy = np.reshape(np.transpose(np.cos(np.deg2rad(the))) * np.sin(np.deg2rad(phi)), Nobs)
        gridz = np.reshape(np.transpose(np.sin(np.deg2rad(the))) * np.ones((1, np.size(phi, 1))), Nobs)

        # Source
        P = sig[:, int(self.t1 * fs):int((self.t1 + self.t2) * fs)]

        # Filtrage des signaux

        freq = np.concatenate(
            (np.atleast_2d(np.arange(0, fs / 2, 1)), np.atleast_2d(np.arange(fs / 2, 0, -1))), axis=1)

        r_A = (12194 ** 2) * (freq ** 4) / \
              ((freq ** 2 + 20.6 ** 2) * ((freq ** 2 + 107.7 ** 2) *
                                          (freq ** 2 + 737.9 ** 2)) ** 0.5 * (freq ** 2 + 12194 ** 2))
        r_A_1000 = (12194 ** 2) * (1000 ** 4) / ((1000 ** 2 + 20.6 ** 2) * ((1000 ** 2 + 107.7 ** 2) *
                                                                            (1000 ** 2 + 737.9 ** 2)) ** 0.5 *
                                                 (1000 ** 2 + 12194 ** 2))
        r_A = r_A / r_A_1000

        # math.floor(Ls)

        signal_gl = np.zeros((self.nbMic, np.size(P, 1)))
        b, a = signal.butter(2, np.array([self.f1, self.f2]) / fs * 2, btype='bandpass')

        for imic1 in np.arange(self.nbMic):
            signal_gl[imic1, :] = signal.filtfilt(b, a, np.atleast_2d(P[imic1, :]))

        fft_pp = np.zeros((self.nbMic, Nfft), dtype=complex)
        Pp = np.zeros((self.nbMic, Nfft))
        for uu in np.arange(self.nbMic):
            # if self.pondA.isChecked():
            # Pour avoir les données en dBA
            fft_pp[uu, :] = ff.fft(np.atleast_2d(signal_gl[uu, :]), n=Nfft) * r_A
            # else:
            #     fft_pp[uu, :] = ff.fft(np.atleast_2d(signal_gl[uu, :]), n=Nfft)

            Pp[uu, :] = np.real(ff.ifft(fft_pp[uu, :]))

        Cxx2_gl = np.zeros((np.size(comb, 0), Nobs))
        for imic in np.arange(np.size(comb, 0)):
            dist_E = (Ax[comb[imic, 0]] * gridx) + (Ay[comb[imic, 0]] * gridy) + (Az[comb[imic, 0]] * gridz)
            dist_R = (Ax[comb[imic, 1]] * gridx) + (Ay[comb[imic, 1]] * gridy) + (Az[comb[imic, 1]] * gridz)
            Tau = (dist_E - dist_R) / c0 * fs

            Ncorr = math.floor(np.max(np.abs(Tau))) + 1
            lag = np.arange(-Ncorr - 1, Ncorr + 1, 1)

            fE = np.atleast_2d(fft_pp[comb[imic, 0], :])
            fR = np.atleast_2d(fft_pp[comb[imic, 1], :])

            cC2 = np.real(ff.ifft(fE * np.conj(fR)))
            Rpm = (1 / Nfft) * np.concatenate((cC2[0, np.size(cC2, 1) - Ncorr - 1:], cC2[0, :Ncorr + 1]))

            Cxx2_gl[imic, :] = np.atleast_2d(np.interp(Tau, lag, Rpm))

        out_bf = np.mean(Cxx2_gl, axis=0)
        out_bf[out_bf < 0] = 0

        outp = np.reshape(10 * np.log10(out_bf / 4e-10), (np.size(the, 1), np.size(phi, 1)))
        outp_max = 10 * np.log10(np.max(out_bf / 4e-10))

        # lignes,colonnes = outp.shape
        # for i in range(lignes):
        #     for j in range(colonnes):
        #         outp[i,j] = outp[i,j]/outp_max


        plt.pcolormesh(np.reshape(phi, np.size(phi, 1)), np.reshape(the, np.size(the, 1)),
                       outp - outp_max, cmap=self.noiseDataColormap)
        plt.axis('off')
        plt.savefig('noise_angle.png', bbox_inches='tight', pad_inches=0)

    def display_image_to_label(self, myLabel, path, colormap):
        imgGray = self.image2gray(path)
        pixmap = self.array2pixmap(imgGray, colormap)
        width = myLabel.frameGeometry().width()
        height = myLabel.frameGeometry().height()
        pixmapScaled = pixmap.scaled(height, width, QtCore.Qt.KeepAspectRatio)
        myLabel.setAlignment(QtCore.Qt.AlignCenter)
        myLabel.setPixmap(pixmapScaled)
        return pixmap

    def image2gray(self, path):
        img = cv2.imread(path, 0)
        return img

    def array2pixmap(self, array, colormap):
        sm = cm.ScalarMappable(cmap=colormap)
        rgbImage = sm.to_rgba(array, bytes=True, norm=False)
        qImg = QImage(rgbImage, rgbImage.shape[1], rgbImage.shape[0], rgbImage.shape[1] * 4, QImage.Format_RGBA8888)
        pix = QPixmap(qImg)
        return pix

    def set_noise_colormap(self, colormap):
        self.noiseDataColormap = colormap
        if self.noiseDataPath != '':
            self.display_image_to_label(self.LA_noiseData, self.noiseDataPath, self.noiseDataColormap)
            if self.mergeDataButtonClicks > 0:
                self.display_image_to_label(self.LA_finalImage, self.noiseDataPath, self.noiseDataColormap)

    def enable_merge_mata_button(self):
        if self.fromCameraButtonClicks > 0 or self.fromComputerButtonClicks > 0:
            if self.loadNoiseFileButtonClicks > 0:
                self.PB_mergeData.setEnabled(True)

    def merge_data(self):
        self.mergeDataButtonClicks += 1
        undistortBackImage = self.undistort_gopro_image(self.goproBackImagePath)
        undistortFrontImage = self.undistort_gopro_image(self.goproFrontImagePath)
        # combinedGoproImage = self.combine_gopro_image(undistortBackImage, undistortFrontImage)
        # finalImage = self.create_gopro_noise_image(combinedGoproImage, [])
        # self.display_image_to_label(self.LA_finalImage, self.finalImagePath, self.noiseDataColormap)
        self.PB_saveAs.setEnabled(True)
        self.SL_transparencyCmap.setEnabled(True)

    def undistort_gopro_image(self, path):
        K = np.array([[1230, 0., 3104/2],
                      [0., 1230, 3000/2],
                      [0., 0., 1.]])

        # zero distortion coefficients work well for this image
        D = np.array([-0.32, -0.126, 0, 0])

        # use Knew to scale the output
        # Knew = K.copy()
        # Knew[(0, 1), (0, 1)] = 0.2 * Knew[(0, 1), (0, 1)]

        img = self.image2gray(path)
        # dimensions de l'image: 3000 x 3104
        img_undistorted = cv2.fisheye.undistortImage(img, K, D=D)
        cv2.imshow('undistorted', img_undistorted)
        return img_undistorted

    def combine_gopro_image(self, backImg, frontImg):
        return 0

    def create_gopro_noise_image(self, combinedGoproImage, noise):
        return 0

    def save_final_image(self):
        imgGray = self.image2gray(self.noiseDataPath)
        finalImagePixmap = self.array2pixmap(imgGray, self.noiseDataColormap)
        self.save_data(finalImagePixmap)

    def save_data(self, imageToSave):
        fileName = QFileDialog.getSaveFileName(self, 'Save File', 'finalImage', '*.png')
        imageToSave.save(fileName[0], 'png')
