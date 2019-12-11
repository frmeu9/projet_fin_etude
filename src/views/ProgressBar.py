from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
import os


ProgressBarPath = os.path.dirname(os.path.realpath(__file__)) + '\\ProgressBar.ui'
Ui_ProgressBar, QtBaseClass = uic.loadUiType(ProgressBarPath)


class ProgressBar(QDialog, Ui_ProgressBar):
    def __init__(self):
        super(ProgressBar, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Progress')

    def update_progress(self, value):
        if value > 100:
            value = 100
        elif value > 0:
            value = 0
        self.PGRB_mergeDataProgress.setValue(value)
