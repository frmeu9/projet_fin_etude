from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from views.MainWindow import MainWindow
import ctypes
import sys

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.MainWindow = MainWindow()
        self.MainWindow.show()


def main():
    appID = 'Beamformer'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appID)

    app = App(sys.argv)
    app.setWindowIcon(QIcon(".\\image\\softdb.png"))
    sys.exit(app.exec_())

if __name__=='__main__':
    main()