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
        self.goproImagePath = ''
        self.mergeDataButtonClicks = 0
        self.PB_mergeData.setEnabled(False)
        self.PB_saveAs.setEnabled(False)

    def connect_button(self):
        self.PB_fromComputer.clicked.connect(self.load_from_computer)
        self.PB_loadNoiseFile.clicked.connect(self.display_noise_data)
        self.PB_fromCamera.clicked.connect(self.load_from_gopro)
        self.PB_saveAs.clicked.connect(self.save_finale_image)
        self.PB_mergeData.clicked.connect(self.merge_data)

    def load_from_computer(self):
        self.goproImagePath = self.ask_open_filename()
        self.display_image_to_label(self.LA_imageGopro, self.goproImagePath, self.goproColormap)

    def display_noise_data(self):
        self.noiseDataPath = self.ask_open_filename()
        self.display_image_to_label(self.LA_noiseData, self.noiseDataPath, self.noiseDataColormap)
        self.PB_mergeData.setEnabled(True)
        # self.display_data_to_label(self.LA_noiseData)

    def ask_open_filename(self):
        path = QFileDialog.getOpenFileName()
        return path[0]

    def load_from_gopro(self):
        gpCam = GoProCamera.GoPro(constants.auth)
        cameraFile = gpCam.listMedia(True, True)
        # cameraFile = [['100GBACK', 'GPBK0001.MP4', '207900848', '1518187858'],
        #               ['100GBACK', 'GPBK0002.MP4', '75187863', '1518188764'],
        #               ['100GBACK', 'GPBK0006.JPG', '2809450', '1518271226'],
        #               ['100GBACK', 'GPBK0007.MP4', '1835045', '1518874876'],
        #               ['100GBACK', 'GPBK0008.MP4', '873464', '1518884630'],
        #               ['100GBACK', 'GPBK0009.MP4', '151566930', '1518885188'],
        #               ['100GBACK', 'GPBK0010.JPG', '3054955', '1518885454']]
        self.selectGoproFile = SelectGoproFile(cameraFile)
        self.selectGoproFile.exec_()
        imageFileName =  self.selectGoproFile.fileName

        frontCameraPath = '100GFRNT'
        # backCameraPath = '100GBACK'

        # gpCam = GoProCamera.GoPro(constants.auth)
        img_front = gpCam.downloadMedia(frontCameraPath, imageFileName)
        # img = gpCam.downloadMedia(backCameraPath, imageFileName)

    def merge_data(self):
        self.mergeDataButtonClicks += 1
        self.display_image_to_label(self.LA_finalImage, self.noiseDataPath, self.noiseDataColormap)
        self.PB_saveAs.setEnabled(True)

    def save_finale_image(self):
        img_gray = self.image2gray(self.noiseDataPath)
        finalImagePixmap = self.array2pixmap(img_gray, self.noiseDataColormap)
        self.save_data(finalImagePixmap)

    def save_data(self, imageToSave):
        fileName = QFileDialog.getSaveFileName(self, 'Save File', 'finalImage', '*.png')
        imageToSave.save(fileName[0], 'png')

    def display_image_to_label(self, myLabel, path, colormap):
        img_gray = self.image2gray(path)
        pixmap = self.array2pixmap(img_gray, colormap)
        width = myLabel.frameGeometry().width()
        height = myLabel.frameGeometry().height()
        pixmap_scaled = pixmap.scaled(height, width, QtCore.Qt.KeepAspectRatio)
        myLabel.setAlignment(QtCore.Qt.AlignCenter)
        myLabel.setPixmap(pixmap_scaled)
        return pixmap

    def display_data_to_label(self, myLabel, path, colormap):
        pass

    def image2gray(self, path):
        img = cv2.imread(path, 0)
        return img

    def array2pixmap(self, array, colormap):
        sm = cm.ScalarMappable(cmap=colormap)
        rgb_im = sm.to_rgba(array, bytes=True, norm=False)
        qim = QImage(rgb_im, rgb_im.shape[1], rgb_im.shape[0], rgb_im.shape[1]*4, QImage.Format_RGBA8888)
        pix = QPixmap(qim)
        return pix

    def set_noise_colormap(self, colormap):
        self.noiseDataColormap = colormap
        if self.noiseDataPath != '':
            if self.mergeDataButtonClicks > 0:
                self.display_image_to_label(self.LA_finalImage, self.noiseDataPath, self.noiseDataColormap)
            self.display_image_to_label(self.LA_noiseData, self.noiseDataPath, self.noiseDataColormap)
