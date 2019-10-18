from PyQt5.QtWidgets import QWidget, QFileDialog, QComboBox, QHBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import uic, QtCore
from matplotlib import cm
import urllib.request
# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.image as mpimg
from goprocam import GoProCamera, constants
from views.SelectGoproFile import SelectGoproFile
import cv2
import os
from bs4 import BeautifulSoup
import requests

MergeDataWidgetPath = os.path.dirname(os.path.realpath(__file__)) + '\\MergeDataWidget.ui'
Ui_MergeDataWidget, QtBaseClass = uic.loadUiType(MergeDataWidgetPath)


class MergeDataWidget(QWidget, Ui_MergeDataWidget):
    def __init__(self):
        super(MergeDataWidget, self).__init__()
        self.setupUi(self)
        self.connect_button()
        self.goproColormap = 'gray'
        self.noiseDataColormap = 'gray'
        self.noiseDataPath = ''
        self.goproFrontImagePath = ''
        self.goproBackImagePath = ''
        self.mergeDataButtonClicks = 0
        self.PB_mergeData.setEnabled(False)
        self.PB_saveAs.setEnabled(False)
        self.PB_fromCamera.setEnabled(False)

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
            self.goproBackImagePath = self.ask_open_filename('Choose back GoPro Image')
            self.display_image_to_label(self.LA_imageGoproBack, self.goproBackImagePath, self.goproColormap)
        except TypeError:
            self.PB_fromCamera.setEnabled(True)

    def display_noise_data(self):
        self.noiseDataPath = self.ask_open_filename('Choose Noise File')
        self.display_image_to_label(self.LA_noiseData, self.noiseDataPath, self.noiseDataColormap)
        self.PB_mergeData.setEnabled(True)
        # self.display_data_to_label(self.LA_noiseData)

    def ask_open_filename(self, windowTitle):
        path = QFileDialog.getOpenFileName(self, windowTitle)
        return path[0]

    def load_from_gopro(self):
        try:
            # gpCam = GoProCamera.GoPro(constants.auth)
            # cameraDir = gpCam.getMediaFusion()
            # mediaInfo = gpCam.getMediaInfo(')
            # print(mediaInfo)
            cameraDir = ['http://10.5.5.9/videos/DCIM/100GBACK/GPFR0010.JPG',
                         'http://10.5.5.9/videos2/DCIM/100GFRNT/GPFR0010.JPG']
            cameraDir[0] = cameraDir[0][0:37]
            cameraDir[1] = cameraDir[1][0:38]
            print(cameraDir)

            # cameraFile = []
            cameraFile = [['100GBACK', 'GPBK0001.MP4', '207900848', '1518187858'],
                          ['100GBACK', 'GPBK0002.MP4', '75187863', '1518188764'],
                          ['100GBACK', 'GPBK0006.JPG', '2809450', '1518271226'],
                          ['100GBACK', 'GPBK0007.MP4', '1835045', '1518874876'],
                          ['100GBACK', 'GPBK0008.MP4', '873464', '1518884630'],
                          ['100GBACK', 'GPBK0009.MP4', '151566930', '1518885188'],
                          ['100GBACK', 'GPBK0010.JPG', '3054955', '1518885454']]
            #
            # for file in self.get_online_file(cameraDir[1]):
            #     cameraFile.append(cameraDir[1][0:15] +  file)
            #
            #
            # print(cameraFile)

            self.selectGoproFile = SelectGoproFile(cameraFile)
            self.selectGoproFile.exec_()
            imageFileName =  self.selectGoproFile.fileName
            print(imageFileName)

        except AttributeError:
            self.PB_fromCamera.setEnabled(False)
            self.load_from_computer()

    def get_online_file(self, url):
        ext = '.JPG'
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        return [node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

    def merge_data(self):
        self.mergeDataButtonClicks += 1
        self.display_image_to_label(self.LA_finalImage, self.noiseDataPath, self.noiseDataColormap)
        self.PB_saveAs.setEnabled(True)

    def save_final_image(self):
        imgGray = self.image2gray(self.noiseDataPath)
        finalImagePixmap = self.array2pixmap(imgGray, self.noiseDataColormap)
        self.save_data(finalImagePixmap)

    def save_data(self, imageToSave):
        fileName = QFileDialog.getSaveFileName(self, 'Save File', 'finalImage', '*.png')
        imageToSave.save(fileName[0], 'png')

    def display_image_to_label(self, myLabel, path, colormap):
        imgGray = self.image2gray(path)
        pixmap = self.array2pixmap(imgGray, colormap)
        width = myLabel.frameGeometry().width()
        height = myLabel.frameGeometry().height()
        pixmapScaled = pixmap.scaled(height, width, QtCore.Qt.KeepAspectRatio)
        myLabel.setAlignment(QtCore.Qt.AlignCenter)
        myLabel.setPixmap(pixmapScaled)
        return pixmap

    def display_data_to_label(self, myLabel, path, colormap):
        pass

    def image2gray(self, path):
        img = cv2.imread(path, 0)
        return img

    def array2pixmap(self, array, colormap):
        sm = cm.ScalarMappable(cmap=colormap)
        rgbImage = sm.to_rgba(array, bytes=True, norm=False)
        qImg = QImage(rgbImage, rgbImage.shape[1], rgbImage.shape[0], rgbImage.shape[1]*4, QImage.Format_RGBA8888)
        pix = QPixmap(qImg)
        return pix

    def set_noise_colormap(self, colormap):
        self.noiseDataColormap = colormap
        if self.noiseDataPath != '':
            if self.mergeDataButtonClicks > 0:
                self.display_image_to_label(self.LA_finalImage, self.noiseDataPath, self.noiseDataColormap)
            self.display_image_to_label(self.LA_noiseData, self.noiseDataPath, self.noiseDataColormap)
