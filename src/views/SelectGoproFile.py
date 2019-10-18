from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
import os


SelectGoproFilePath = os.path.dirname(os.path.realpath(__file__)) + '\\SelectGoproFile.ui'
Ui_SelectGoproFile, QtBaseClass = uic.loadUiType(SelectGoproFilePath)


class SelectGoproFile(QDialog, Ui_SelectGoproFile):
    def __init__(self, cameraFileList):
        super(SelectGoproFile, self).__init__()
        self.setupUi(self)
        self.connect_button()
        self.setWindowTitle('Select GoPro Image')
        self.fileName = ''

        for i in range(len(cameraFileList)):
            fileName = cameraFileList[i]
            self.LI_goproFilename.addItem(fileName)

    def connect_button(self):
        self.PB_selectGoproFile.clicked.connect(self.get_gopro_filename)

    def get_gopro_filename(self):
        listItems = self.LI_goproFilename.selectedItems()
        x = []

        for i in range(len(listItems)):
            x.append(str(self.LI_goproFilename.selectedItems()[i].text()))

        self.fileName = x[0]
        # print(self.fileName)
        self.close()
