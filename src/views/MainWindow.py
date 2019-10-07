from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import os
from views.MergeDataWidget import MergeDataWidget


MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '\\MainWindow.ui'
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.MergeDataWidget = MergeDataWidget()
        self.setCentralWidget(self.MergeDataWidget)
        self.connect_menu()

    def connect_menu(self):
        self.MN_file_exit.triggered.connect(self.exit_main_window)
        self.MN_options_colormap_viridis.triggered.connect(self.chosen_colormap)
        self.MN_options_colormap_magma.triggered.connect(self.chosen_colormap)
        self.MN_options_colormap_gray.triggered.connect(self.chosen_colormap)
        self.MN_help_documentations.triggered.connect(self.menu_help_docs)
        self.MN_help_acknowledgement.triggered.connect(self.menu_help_acknow)

    def exit_main_window(self):
        self.close()

    def chosen_colormap(self):
        choice = self.sender()
        colormap = choice.text()
        self.MergeDataWidget.set_noise_colormap(colormap)

    def menu_help_docs(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("How this software works: \n"
                       "1. Load a 360 photo, from computer or from camera. \n"
                       "2. Load noise file from computer. \n"
                       "3. Merge data: The software will layout the noise data to the 360 photo. \n")
        msgBox.setWindowTitle("Documentations")
        msgBox.exec_()

    def menu_help_acknow(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Acknowledgement: \n Thanks to PYMARC2 for helping with the programmation \n"
                       "(and the css stylesheet). ")
        msgBox.setWindowTitle("Acknowledgement")
        msgBox.exec_()
