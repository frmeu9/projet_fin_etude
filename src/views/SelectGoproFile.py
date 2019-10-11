from PyQt5.QtWidgets import QWidget, QFileDialog, QComboBox, QHBoxLayout, QDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import uic, QtCore
from matplotlib import cm
# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.image as mpimg
from goprocam import GoProCamera, constants
import cv2
import os

SelectGoproFilePath = os.path.dirname(os.path.realpath(__file__)) + '\\SelectGoproFile.ui'
Ui_SelectGoproFile, QtBaseClass = uic.loadUiType(SelectGoproFilePath)

class SelectGoproFile(QDialog, Ui_SelectGoproFile):
    def __init__(self, cameraFileList):
        super(SelectGoproFile, self).__init__()
        self.setupUi(self)
        self.connectButton()
        self.fileName = ''

        for i in range(len(cameraFileList)):
            fileName = cameraFileList[i][1]
            self.LI_goproFilename.addItem(fileName)

    def connectButton(self):
        self.PB_selectGoproFile.clicked.connect(self.get_gopro_filename)

    def get_gopro_filename(self):
        items = self.LI_goproFilename.selectedItems()
        x = []

        for i in range(len(items)):
            x.append(str(self.LI_goproFilename.selectedItems()[i].text()))

        self.fileName = x[0]
        print(self.fileName)
        self.close()