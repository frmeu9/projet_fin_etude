from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from goprocam import GoProCamera, constants
import os

MergeDataWidgetPath = os.path.dirname(os.path.realpath(__file__)) + '\\MergeDataWidget.ui'
Ui_MergeDataWidget, QtBaseClass = uic.loadUiType(MergeDataWidgetPath)

class MergeDataWidget(QWidget, Ui_MergeDataWidget):
    def __init__(self):
        super(MergeDataWidget, self).__init__()
        self.setupUi(self)
        self.connect_button()

    def connect_button(self):
        self.PB_fromComputer.clicked.connect(self.display_gopro_image)
        self.PB_loadNoiseFile.clicked.connect(self.display_noise_data)

    def display_gopro_image(self):
        path = self.ask_open_filename()
        self.display_image_to_label(self.LA_imageGopro, path)

    def display_noise_data(self):
        path = self.ask_open_filename()
        self.display_image_to_label(self.LA_noiseData, path)

    def ask_open_filename(self):
        path = QFileDialog.getOpenFileName()
        print(path)
        return path[0]

    def load_from_gopro(self):
        gpCam = GoProCamera.GoPro(constants.auth)
        fileList = gpCam.listMedia(True, True)
        gpCam.mode("1")
        folder = cameraFile[0]
        file = cameraFile[1]
        time.sleep(8)
        self.img = gpCam.downloadMedia(folder, file)

    def merge_data(self):
        pass

    def save_as(self):
        pass

    def display_image_to_label(self, myLabel, path):
        pixmap = QPixmap(path)
        myLabel.setPixmap(pixmap)