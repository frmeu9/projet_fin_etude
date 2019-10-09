from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import uic, QtCore
from matplotlib import cm
# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.image as mpimg
# from goprocam import GoProCamera, constants
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

    def connect_button(self):
        self.PB_fromComputer.clicked.connect(self.display_gopro_image)
        self.PB_loadNoiseFile.clicked.connect(self.display_noise_data)
        self.PB_fromCamera.clicked.connect(self.load_from_gopro)
        self.PB_saveAs.clicked.connect(self.save_as)
        self.PB_mergeData.clicked.connect(self.merge_data)

    def display_gopro_image(self):
        self.goproImagePath = self.ask_open_filename()
        self.display_image_to_label(self.LA_imageGopro, self.goproImagePath, self.goproColormap)

    def display_noise_data(self):
        self.noiseDataPath = self.ask_open_filename()
        self.display_image_to_label(self.LA_noiseData, self.noiseDataPath, self.noiseDataColormap)
        # self.display_data_to_label(self.LA_noiseData)

    def ask_open_filename(self):
        path = QFileDialog.getOpenFileName()
        return path[0]

    def load_from_gopro(self):
        # gpCam = GoProCamera.GoPro(constants.auth)
        # cameraFile = gpCam.listMedia(True, True)
        # gpCam.KeepAlive()
        # gpCam.mode("1")
        # folder = cameraFile[0]
        # file = cameraFile[1]
        # gpCam.mode("1")
        # gpCam.KeepAlive()
        # self.img = gpCam.downloadMedia(folder, file)
        pass

    def merge_data(self):
        self.mergeDataButtonClicks += 1
        self.display_image_to_label(self.LA_finalImage, self.noiseDataPath, self.noiseDataColormap)

    def save_as(self):
        img_gray = self.image2gray(self.noiseDataPath)
        finalImagePixmap = self.array2pixmap(img_gray, self.noiseDataColormap)
        fileName = QFileDialog.getSaveFileName(self, 'Save File', 'finalImage', '*.png')
        finalImagePixmap.save(fileName[0], 'png')

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
