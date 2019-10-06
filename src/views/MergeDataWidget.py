from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import uic
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
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
        self.colormap = 'gray'
        self.noiseDataPath = ''

    def connect_button(self):
        self.PB_fromComputer.clicked.connect(self.display_gopro_image)
        self.PB_loadNoiseFile.clicked.connect(self.display_noise_data)
        self.PB_saveAs.clicked.connect(self.save_as)

    def display_gopro_image(self):
        path = self.ask_open_filename()
        self.colormap = 'gray'
        self.display_image_to_label(self.LA_imageGopro, path)

    def display_noise_data(self):
        self.noiseDataPath = self.ask_open_filename()
        self.display_image_to_label(self.LA_noiseData, self.noiseDataPath)
        #self.display_data_to_label(self.LA_noiseData, path)

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
        pass

    def save_as(self):
        # p = self.array2pixmap()
        # fileName = QFileDialog.getSaveFileName(self, 'Save File', '', '*.jpg')
        # p.save(fileName, "PNG")
        pass

    def display_image_to_label(self, myLabel, path):
        img_gray = self.image2gray(path)
        pixmap = self.array2pixmap(img_gray)
        myLabel.setPixmap(pixmap)

    def display_data_to_label(self, myLabel, path):
        pass

    def image2gray(self, path):
        img = cv2.imread(path,0)
        return img

    def array2pixmap(self, array):
        sm = cm.ScalarMappable(cmap=self.colormap)
        rgb_im = sm.to_rgba(array, bytes=True, norm=False)
        qim = QImage(rgb_im, rgb_im.shape[1], rgb_im.shape[0], rgb_im.shape[1]*4, QImage.Format_RGBA8888)
        pix = QPixmap(qim)
        return pix

    def define_colormap(self, colormap):
        if self.noiseDataPath == '':
            self.colormap = colormap
        else:
            self.colormap = colormap
            self.display_image_to_label(self.LA_noiseData, self.noiseDataPath)
