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
from PIL import Image
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
        self.noiseDataColormap = 'magma'
        self.noiseDataPath = ''
        self.goproFrontImagePath = ''
        self.goproBackImagePath = ''
        self.combinedImagesPath = ''
        self.finalImagePath = ''

        self.f1 = None
        self.f2 = None
        self.Ar = None
        self.Athe = None
        self.Aphi = None
        self.nbMic = None
        self.fs = None
        self.sig = None
        self.t1 = None
        self.t2 = None
        self.outp = None
        self.outpMax = None
        self.the = None
        self.phi = None
        self.fov = 186

        self.PB_mergeData.setEnabled(False)
        self.PB_saveAs.setEnabled(False)
        self.PB_fromCamera.setEnabled(False)
        self.SB_time1.setMinimum(0)
        self.SB_time1.setMaximum(30)
        self.SB_time2.setMinimum(0)
        self.SB_time2.setMaximum(30)
        self.SB_frequency1.setMinimum(1)
        self.SB_frequency1.setMaximum(20000)
        self.SB_frequency2.setMinimum(1)
        self.SB_frequency2.setMaximum(20000)

        self.SB_time1.setValue(1)
        self.SB_time2.setValue(2)
        self.SB_frequency1.setValue(20)
        self.SB_frequency2.setValue(20000)

        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.scriptDir = scriptDir[:-5].replace(os.sep, '/')

    def connect_button(self):
        self.PB_fromComputer.clicked.connect(self.load_from_computer)
        self.PB_loadNoiseFile.clicked.connect(self.load_noise_data)
        self.PB_fromCamera.clicked.connect(self.load_from_gopro)
        self.PB_updateFFT.clicked.connect(self.update_FFT)
        self.PB_saveAs.clicked.connect(self.save_final_image)
        self.PB_mergeData.clicked.connect(self.merge_data)

    def load_from_computer(self):
        try:
            self.goproFrontImagePath = self.ask_open_filename('Choose front GoPro Image')
            self.display_image_to_label(self.LA_imageGoproFront, self.goproFrontImagePath, self.goproColormap)
            self.goproBackImagePath = self.goproFrontImagePath.replace('GPFR', 'GPBK')
            self.display_image_to_label(self.LA_imageGoproBack, self.goproBackImagePath, self.goproColormap)
            self.enable_merge_data_button()
        except TypeError:
            self.PB_fromCamera.setEnabled(True)

    def ask_open_filename(self, windowTitle):
        path = QFileDialog.getOpenFileName(self, windowTitle)
        return path[0]

    def load_from_gopro(self):
        try:
            self.get_gopro_content()
            # print(self.goproFrontImagePath, self.goproBackImagePath)
            self.enable_merge_data_button()
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

    def load_noise_data(self):
        self.noiseDataPath = ''
        script_dir = os.path.dirname(os.path.realpath(__file__))
        self.wav_file_open(script_dir)
        self.noiseDataPath = self.scriptDir + 'noise_angle.png'
        self.update_FFT()

    def fft_parameter_change(self):
        t1 = self.SB_time1.value()
        t2 = self.SB_time2.value()
        f1 = self.SB_frequency1.value()
        f2 = self.SB_frequency2.value()
        if t2 < t1:
            self.SB_time2.setValue(t1+1)
        elif f2 < f1:
            self.SB_frequency2.setValue(f1 + 1)

    def update_FFT(self):
        try:
            self.fft_parameter_change()
            self.get_angle(self.fs, self.sig)
            self.display_image_to_label(self.LA_noiseData, self.noiseDataPath)
            self.enable_merge_data_button()
        except TypeError:
            self.load_noise_data()

    def wav_file_open(self, scriptDir):
        # Fonction tirée du script Beamforming3D de Soft dB
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', os.path.expanduser("~/Desktop"),
                                                         'Wave Files (*.wav)')
        if fname != '':
            fs, sig = wavfile.read(fname)
            Ls = np.size(sig, 0) / fs
            Time = np.arange(0, np.size(sig, 0), 1) / fs

            sens = pd.read_excel(os.path.join(scriptDir, "Supplements/Sensibilite_microphones.xlsx"), header=None)
            sens = np.transpose(np.atleast_2d(sens.iloc[1:, 2].values.astype('float64')))
            sig = np.transpose(sig) * sens

            tmp = pd.read_excel(os.path.join(scriptDir, "Supplements/Position_microphones.xlsx"), header=None)
            Scale_Up = tmp.iloc[0, 3]

            self.Aphi = tmp.iloc[3:, 3].values.astype('float64')
            self.Athe = tmp.iloc[3:, 4].values.astype('float64')
            self.Ar = Scale_Up * tmp.iloc[3:, 2].values.astype('float64')

            self.nbMic = len(self.Aphi)

            self.fs = fs
            self.sig = sig

    def get_angle(self, fs, sig):
        self.t1 = self.SB_time1.value()
        self.t2 = self.SB_time2.value()
        self.f1 = self.SB_frequency1.value()
        self.f2 = self.SB_frequency2.value()

        # Fonction tirée du script Beamforming3D de Soft dB
        Nfft = fs
        c0 = 343
        # Coordonnées de l'antenne en dregrés
        Ax = self.Ar * np.cos(np.deg2rad(self.Athe)) * np.cos(np.deg2rad(self.Aphi))
        Ay = self.Ar * np.cos(np.deg2rad(self.Athe)) * np.sin(np.deg2rad(self.Aphi))
        Az = self.Ar * np.sin(np.deg2rad(self.Athe))

        comb = np.array(list(combinations(np.arange(self.nbMic), 2)))

        # Scan zone
        self.phi = np.atleast_2d(np.arange(-180, 181, 1))
        self.the = np.atleast_2d(np.arange(-90, 91, 1))
        Nobs = np.size(self.phi, 1) * np.size(self.the, 1)

        gridx = np.reshape(np.transpose(np.cos(np.deg2rad(self.the))) * np.cos(np.deg2rad(self.phi)), Nobs)
        gridy = np.reshape(np.transpose(np.cos(np.deg2rad(self.the))) * np.sin(np.deg2rad(self.phi)), Nobs)
        gridz = np.reshape(np.transpose(np.sin(np.deg2rad(self.the))) * np.ones((1, np.size(self.phi, 1))), Nobs)

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

        self.out_bf = np.mean(Cxx2_gl, axis=0)
        self.out_bf[self.out_bf < 0] = 0

        self.outp = np.reshape(10 * np.log10(self.out_bf / 4e-10), (np.size(self.the, 1), np.size(self.phi, 1)))
        self.outpMax = 10 * np.log10(np.max(self.out_bf / 4e-10))

        plt.pcolormesh(np.reshape(self.phi, np.size(self.phi, 1)), np.reshape(self.the, np.size(self.the, 1)),
                       self.outp - self.outpMax, cmap=self.noiseDataColormap)
        # os.remove(self.noiseDataPath)
        plt.axis('off')
        plt.savefig('noise_angle.png', bbox_inches='tight', pad_inches=0, transparent=True)
        plt.close()

    def display_image_to_label(self, myLabel, path, colormap=None):
        pixmap = None
        if colormap != None:
            imgGray = self.image2gray(path)
            pixmap = self.array2pixmap(imgGray, colormap)
        if colormap == None:
            pixmap = QPixmap(path)
        width = myLabel.frameGeometry().width()
        height = myLabel.frameGeometry().height()
        pixmapScaled = pixmap.scaled(height, width, QtCore.Qt.KeepAspectRatio)
        myLabel.setAlignment(QtCore.Qt.AlignCenter)
        myLabel.setPixmap(pixmapScaled)

    def image2gray(self, path):
        img = cv2.imread(path, 0)
        return img

    def array2pixmap(self, array=None, colormap=None):
        pix = None
        if colormap != None:
            sm = cm.ScalarMappable(cmap=colormap)
            rgbImage = sm.to_rgba(array, bytes=True, norm=False)
            qImg = QImage(rgbImage, rgbImage.shape[1], rgbImage.shape[0], rgbImage.shape[1] * 4, QImage.Format_RGBA8888)
            pix = QPixmap(qImg)
        if colormap == None and array == None:
            pix = QPixmap(self.finalImagePath)
        return pix

    def set_noise_colormap(self, colormap):
        self.noiseDataColormap = colormap
        if self.noiseDataPath != '':
            self.update_FFT()
            if self.combinedImagesPath != '':
                self.overlay_gopro_noise()
                self.display_image_to_label(self.LA_finalImage, self.finalImagePath)

    def enable_merge_data_button(self):
        if self.goproBackImagePath != '' and self.goproFrontImagePath != '' and self.noiseDataPath != '':
                self.PB_mergeData.setEnabled(True)

    def merge_data(self):
        back = self.unwarp_image(self.goproBackImagePath)
        front = self.unwarp_image(self.goproFrontImagePath)
        self.combine_gopro_image(back, front)
        self.overlay_gopro_noise()
        self.finalImagePath = self.scriptDir + 'final_image.png'
        self.display_image_to_label(self.LA_finalImage, self.finalImagePath)
        self.PB_saveAs.setEnabled(True)

    def unwarp_image(self, imgPath):
        img = cv2.imread(imgPath)
        H, W, _ = img.shape
        xMap, yMap = self.build_mapping(W, H, W, H, self.fov)
        imgDewarped = cv2.remap(img, xMap, yMap, cv2.INTER_LINEAR)
        return imgDewarped

    def equirectangular_projection(self, xProj, yProj, W, H, fov):
        """Return the equirectangular projection on a unit sphere,
            given cartesian coordinates of the de-warped image."""
        thetaAlt = xProj * fov / W
        phiAlt = yProj * np.pi / H

        x = np.sin(thetaAlt) * np.cos(phiAlt)
        y = np.sin(phiAlt)
        z = np.cos(thetaAlt) * np.cos(phiAlt)

        return np.arctan2(y, x), np.arctan2(np.sqrt(x ** 2 + y ** 2), z)

    def build_mapping(self, Ws, Hs, Wd, Hd, fov):
        """Return a mapping from de-warped images to fisheye images."""
        fov = fov * np.pi / 180.0

        # cartesian coordinates of the de-warped rectangular image
        ys, xs = np.indices((Hs, Ws), np.float32)
        yProj = Hs / 2.0 - ys
        xProj = xs - Ws / 2.0

        # spherical coordinates
        theta, phi = self.equirectangular_projection(xProj, yProj, Ws, Hs, fov)

        # polar coordinates (of the fisheye image)
        p = Hd * phi / fov

        # cartesian coordinates of the fisheye image
        yFish = p * np.sin(theta)
        xFish = p * np.cos(theta)

        yMap = Hd / 2.0 - yFish
        xMap = Wd / 2.0 + xFish
        return xMap, yMap

    def combine_gopro_image(self, backImg, frontImg):
        _, col, dim = backImg.shape
        backImg = np.vstack((backImg, np.zeros((14, col, dim))))
        frontImg = np.vstack((np.zeros((14, col, dim)), frontImg))
        finalImage = np.hstack((frontImg[:, :col-45], backImg[:, 65:]))
        rows, _, _ = finalImage.shape
        finalImage = finalImage[20:rows-20, :]
        self.combinedImagesPath = self.scriptDir + 'combined_images.png'
        cv2.imwrite(self.combinedImagesPath, finalImage)

    def overlay_gopro_noise(self):
        img = cv2.imread(self.noiseDataPath, cv2.IMREAD_UNCHANGED)
        noiseDataMask = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA))
        goproImageBackground = Image.fromarray(cv2.imread(self.combinedImagesPath)).convert(noiseDataMask.mode)
        goproImageBackground = goproImageBackground.resize(noiseDataMask.size, Image.ANTIALIAS)
        finalImage = Image.blend(goproImageBackground, noiseDataMask, alpha=0.20)
        finalImage.save('final_image.png')

    def save_final_image(self):
        finalImagePixmap = self.array2pixmap()
        self.save_data(finalImagePixmap)

    def save_data(self, imageToSave):
        fileName = QFileDialog.getSaveFileName(self, 'Save File', 'finalImage', '*.png')
        imageToSave.save(fileName[0], 'png')
