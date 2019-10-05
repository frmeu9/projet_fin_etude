from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
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

