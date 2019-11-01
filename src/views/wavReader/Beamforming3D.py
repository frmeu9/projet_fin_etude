
# Form implementation generated from reading ui file 'C:\Users\chris\Documents\Python Scripts\GUI\test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from scipy import signal
import scipy.fftpack as ff
import matplotlib.pyplot as plt
from itertools import combinations
import math
from scipy.io import wavfile
import pandas as pd
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.widgets import Cursor
#import sounddevice as sd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 760)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_t2 = QtWidgets.QLabel(self.centralwidget)
        self.label_t2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_t2.setFont(font)
        self.label_t2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_t2.setObjectName("label_t2")
        self.gridLayout.addWidget(self.label_t2, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 2)
        self.label_t1 = QtWidgets.QLabel(self.centralwidget)
        self.label_t1.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_t1.setFont(font)
        self.label_t1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_t1.setObjectName("label_t1")
        self.gridLayout.addWidget(self.label_t1, 3, 1, 1, 1)
        self.ech_lab = QtWidgets.QLabel(self.centralwidget)
        self.ech_lab.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.ech_lab.setFont(font)
        self.ech_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.ech_lab.setObjectName("ech_lab")
        self.gridLayout.addWidget(self.ech_lab, 12, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pondA = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pondA.setFont(font)
        self.pondA.setChecked(True)
        self.pondA.setObjectName("pondA")
        self.horizontalLayout_2.addWidget(self.pondA)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 9, 1, 2, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bouton_run = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bouton_run.sizePolicy().hasHeightForWidth())
        self.bouton_run.setSizePolicy(sizePolicy)
        self.bouton_run.setMaximumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bouton_run.setFont(font)
        self.bouton_run.setStyleSheet("background-color: rgb(7, 76, 121);")
        self.bouton_run.setObjectName("bouton_run")
        self.horizontalLayout_3.addWidget(self.bouton_run)
        self.gridLayout.addLayout(self.horizontalLayout_3, 13, 1, 1, 2)
        self.ech_plot = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ech_plot.setMinimumSize(QtCore.QSize(0, 0))
        self.ech_plot.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.ech_plot.setFont(font)
        self.ech_plot.setDecimals(1)
        self.ech_plot.setMinimum(0.0)
        self.ech_plot.setMaximum(9999.0)
        self.ech_plot.setSingleStep(0.5)
        self.ech_plot.setProperty("value", 1.0)
        self.ech_plot.setObjectName("ech_plot")
        self.gridLayout.addWidget(self.ech_plot, 12, 2, 1, 1)
        self.label_f1 = QtWidgets.QLabel(self.centralwidget)
        self.label_f1.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_f1.setFont(font)
        self.label_f1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_f1.setObjectName("label_f1")
        self.gridLayout.addWidget(self.label_f1, 6, 1, 1, 1)
        self.in_f2 = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_f2.sizePolicy().hasHeightForWidth())
        self.in_f2.setSizePolicy(sizePolicy)
        self.in_f2.setMinimumSize(QtCore.QSize(70, 0))
        self.in_f2.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.in_f2.setFont(font)
        self.in_f2.setMinimum(1)
        self.in_f2.setMaximum(99999)
        self.in_f2.setSingleStep(100)
        self.in_f2.setProperty("value", 2000)
        self.in_f2.setObjectName("in_f2")
        self.gridLayout.addWidget(self.in_f2, 7, 2, 1, 1)
        self.in_t1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.in_t1.setMinimumSize(QtCore.QSize(70, 0))
        self.in_t1.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.in_t1.setFont(font)
        self.in_t1.setDecimals(3)
        self.in_t1.setMaximum(9999.99)
        self.in_t1.setObjectName("in_t1")
        self.gridLayout.addWidget(self.in_t1, 4, 1, 1, 1)
        self.in_t2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.in_t2.setMinimumSize(QtCore.QSize(70, 0))
        self.in_t2.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.in_t2.setFont(font)
        self.in_t2.setDecimals(3)
        self.in_t2.setMaximum(9999.99)
        self.in_t2.setProperty("value", 1.0)
        self.in_t2.setObjectName("in_t2")
        self.gridLayout.addWidget(self.in_t2, 4, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 8, 1, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 11, 1, 1, 1)
        self.in_f1 = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_f1.sizePolicy().hasHeightForWidth())
        self.in_f1.setSizePolicy(sizePolicy)
        self.in_f1.setMinimumSize(QtCore.QSize(70, 0))
        self.in_f1.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.in_f1.setFont(font)
        self.in_f1.setMinimum(1)
        self.in_f1.setMaximum(99999)
        self.in_f1.setSingleStep(100)
        self.in_f1.setProperty("value", 100)
        self.in_f1.setObjectName("in_f1")
        self.gridLayout.addWidget(self.in_f1, 7, 1, 1, 1)
        self.plot_time = plot_time(self.centralwidget)
        self.plot_time.setMinimumSize(QtCore.QSize(0, 300))
        self.plot_time.setMaximumSize(QtCore.QSize(16777215, 400))
        self.plot_time.setStyleSheet("")
        self.plot_time.setObjectName("plot_time")
        self.gridLayout.addWidget(self.plot_time, 0, 3, 1, 2)
        self.label_f2 = QtWidgets.QLabel(self.centralwidget)
        self.label_f2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_f2.setFont(font)
        self.label_f2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_f2.setObjectName("label_f2")
        self.gridLayout.addWidget(self.label_f2, 6, 2, 1, 1)
        self.plot_bf = plot_bf(self.centralwidget)
        self.plot_bf.setMinimumSize(QtCore.QSize(350, 300))
        self.plot_bf.setStyleSheet("")
        self.plot_bf.setObjectName("plot_bf")
        self.gridLayout.addWidget(self.plot_bf, 1, 3, 15, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setMinimumSize(QtCore.QSize(0, 70))
        self.label_logo.setMaximumSize(QtCore.QSize(204, 100))
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout_4.addWidget(self.label_logo)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.open_button.setFont(font)
        self.open_button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.open_button.setObjectName("open_button")
        self.horizontalLayout.addWidget(self.open_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.bouton_t1 = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_t1.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bouton_t1.setFont(font)
        self.bouton_t1.setStyleSheet("background-color: rgb(204, 204, 204);\n"
"color: rgb(0, 170, 255);")
        self.bouton_t1.setCheckable(True)
        self.bouton_t1.setDefault(False)
        self.bouton_t1.setFlat(False)
        self.bouton_t1.setObjectName("bouton_t1")
        self.horizontalLayout_5.addWidget(self.bouton_t1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.bouton_t2 = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_t2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bouton_t2.setFont(font)
        self.bouton_t2.setStyleSheet("background-color: rgb(204, 204, 204);\n"
"color: rgb(7, 76, 121);")
        self.bouton_t2.setCheckable(True)
        self.bouton_t2.setObjectName("bouton_t2")
        self.horizontalLayout_5.addWidget(self.bouton_t2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
#        self.bouton_sound = QtWidgets.QPushButton(self.centralwidget)
#        self.bouton_sound.setMaximumSize(QtCore.QSize(30, 16777215))
#        font = QtGui.QFont()
#        font.setFamily("Calibri")
#        font.setPointSize(14)
#        font.setBold(False)
#        font.setWeight(50)
#        self.bouton_sound.setFont(font)
#        self.bouton_sound.setStyleSheet("")
#        self.bouton_sound.setText("")
#        self.bouton_sound.setCheckable(False)
#        self.bouton_sound.setObjectName("bouton_sound")
#        self.horizontalLayout_5.addWidget(self.bouton_sound)
#        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#        self.horizontalLayout_5.addItem(spacerItem11)
#        self.bouton_sound_stop = QtWidgets.QPushButton(self.centralwidget)
#        self.bouton_sound_stop.setMaximumSize(QtCore.QSize(30, 16777215))
#        font = QtGui.QFont()
#        font.setFamily("Calibri")
#        font.setPointSize(14)
#        font.setBold(False)
#        font.setWeight(50)
#        self.bouton_sound_stop.setFont(font)
#        self.bouton_sound_stop.setStyleSheet("")
#        self.bouton_sound_stop.setText("")
#        self.bouton_sound_stop.setCheckable(False)
#        self.bouton_sound_stop.setObjectName("bouton_sound_stop")
#        self.horizontalLayout_5.addWidget(self.bouton_sound_stop)
#        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#        self.horizontalLayout_5.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.script_dir = os.path.dirname(__file__)

#        self.bouton_sound.setIcon(QtGui.QIcon(os.path.join(self.script_dir,'Supplements\logo_play.png')))
#        self.bouton_sound.setIconSize(QtCore.QSize(self.bouton_sound.width()-7,self.bouton_sound.height()-7))
#
#        self.bouton_sound_stop.setIcon(QtGui.QIcon(os.path.join(self.script_dir,'Supplements\logo_stop.jpg')))
#        self.bouton_sound_stop.setIconSize(QtCore.QSize(self.bouton_sound_stop.width()-7,self.bouton_sound_stop.height()-7))

        self.pixmap = QtGui.QPixmap(os.path.join(self.script_dir,'Supplements\logo_sdb.png'))
        self.label_logo.setPixmap(self.pixmap.scaled(self.label_logo.width()+110,self.label_logo.height()+110, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation))

        self.bouton_t1.clicked.connect(self.action_t1)
        self.bouton_t2.clicked.connect(self.action_t2)

        self.in_f1.valueChanged.connect(self.reinit_bouton)
        self.in_f2.valueChanged.connect(self.reinit_bouton)
        self.in_t1.valueChanged.connect(self.plot_t1t2)
        self.in_t2.valueChanged.connect(self.plot_t1t2)
        self.ech_plot.valueChanged.connect(self.reinit_bouton)
        self.pondA.clicked.connect(self.reinit_bouton)

#        self.bouton_sound.clicked.connect(self.action_sound)
#        self.bouton_sound_stop.clicked.connect(self.action_sound_stop)

        app.aboutToQuit.connect(self.quit_app)

        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.setStatusTip('Open Wave File')
        self.actionOpen.triggered.connect(self.file_open)

        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.setStatusTip('Quit application')
        self.actionQuit.triggered.connect(self.quit_app)

        self.bouton_run.clicked.connect(self.tracer)
        self.open_button.clicked.connect(self.file_open)
        enterShortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return), self.bouton_run)
        enterShortcut.activated.connect(self.tracer)

        self.infoBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,'Warning: open Wave file first','Open Wave OR Ctrl+O')
        self.infoBox2 = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,'Warning','t1 must be higher than t0')
        self.infoBox3 = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,'Warning','f1 must be lower than f2')
        self.sig = np.zeros(1)
        self.ct_sound = 0
        self.t1c = 0
        self.t2c = 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Beamforming3D"))
        self.label_t2.setText(_translate("MainWindow", "Durée [s]"))
        self.label_t1.setText(_translate("MainWindow", "t0 [s]"))
        self.ech_lab.setText(_translate("MainWindow", "Échelle"))
        self.pondA.setText(_translate("MainWindow", "dBA"))
        self.bouton_run.setText(_translate("MainWindow", "Run Code"))
        self.label_f1.setText(_translate("MainWindow", "f1 [Hz]"))
        self.label_f2.setText(_translate("MainWindow", "f2 [Hz]"))
        self.open_button.setText(_translate("MainWindow", "Open \n"
" Wave"))
        self.bouton_t1.setText(_translate("MainWindow", "t0"))
        self.bouton_t2.setText(_translate("MainWindow", "t1"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open Wave File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit application"))

#    def action_sound(self):
#        self.reinit_bouton()
#        if len(self.sig)<2:
#            self.infoBox.exec()
#        else:
#            sd.play(self.sig[0,int(self.in_t1.value()*self.fs):int((self.in_t1.value()+self.in_t2.value())*self.fs)],self.fs)
#
#    def action_sound_stop(self):
#        self.reinit_bouton()
#        if len(self.sig)<2:
#            self.infoBox.exec()
#        else:
#            sd.stop()

    # def reinit_bouton(self):
    #     if self.bouton_t1.isChecked():
    #         self.bouton_t1.toggle()
    #     if self.bouton_t2.isChecked():
    #         self.bouton_t2.toggle()

    # def plot_t1t2(self):
    #     try:
    #         self.l_t2.remove()
    #     except:
    #         pass
    #
    #     self.l_t2 = self.plot_time.canvas_time.axes_time.axvline(x=(self.in_t2.value()+self.in_t1.value()),color = (7/255, 76/255, 121/255), linestyle='dashed')
    #     self.plot_time.canvas_time.draw()
    #     try:
    #         self.l_t1.remove()
    #     except:
    #         pass
    #
    #     self.l_t1 = self.plot_time.canvas_time.axes_time.axvline(x=self.in_t1.value(),color = (0, 170/255, 1), linestyle='dashed')
    #     self.plot_time.canvas_time.draw()

    def action_t1(self):
        if len(self.sig)<2:
            self.infoBox.exec()
            self.bouton_t1.toggle()
        else:
            self.cid = self.plot_time.canvas_time.mpl_connect('button_press_event', self.onclick_t1)

    def action_t2(self):
        if len(self.sig)<2:
            self.infoBox.exec()
            self.bouton_t2.toggle()
        else:
            self.cid = self.plot_time.canvas_time.mpl_connect('button_press_event', self.onclick_t2)

    def onclick_t1(self,event):
        if self.bouton_t1.isChecked():
            self.t1c = event.xdata
            if self.t1c>(self.in_t1.value() + self.in_t2.value()):
                self.in_t2.setValue(0)
            else:
                self.in_t2.setValue(self.t2c-self.t1c)

            self.in_t1.setValue(self.t1c)
            self.bouton_t1.toggle()
            self.bouton_t2.toggle()
        else:
            if self.bouton_t2.isChecked():
                self.t2c = event.xdata
                self.bouton_t2.toggle()
                if self.t2c<=self.t1c:
                    self.infoBox2.exec()
                else:
                    self.in_t2.setValue(self.t2c-self.t1c)
            else:
                self.plot_time.canvas_time.mpl_disconnect(self.cid)

    def onclick_t2(self,event):
        if self.bouton_t2.isChecked():
            self.t2c = event.xdata
            self.bouton_t2.toggle()
            if self.t2c<=self.t1c:
                self.infoBox2.exec()
            else:
                self.in_t2.setValue(self.t2c-self.t1c)
        else:
            self.plot_time.canvas_time.mpl_disconnect(self.cid)

    def quit_app(self):
        sys.exit()

    def file_open(self, script_dir):

        # self.reinit_bouton()

        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File',os.path.expanduser("~/Desktop"),'Wave Files (*.wav)')

        if self.fname!='':
            # self.open_button.setStyleSheet("background-color: green")
            self.fs, self.sig = wavfile.read(self.fname)
            self.Ls = np.size(self.sig,0)/self.fs
            Time = np.arange(0,np.size(self.sig,0),1)/self.fs

            sens = pd.read_excel(os.path.join(script_dir,"Supplements\Sensibilite_microphones.xlsx"),header=None)
            sens = np.transpose(np.atleast_2d((sens.iloc[1:,2].values).astype('float64')))
            self.sig = np.transpose(self.sig)*sens

#             self.plot_time.canvas_time.axes_time.clear()
#             self.plot_time.canvas_time.axes_time.plot(Time,self.sig[0,])
# #            self.plot_time.canvas_time.axes_time.set_in_layout(True)
#             self.plot_time.canvas_time.axes_time.set_xlabel('Time [s]')
#             self.plot_time.canvas_time.axes_time.set_ylabel('p [Pa]')
#             self.plot_time.canvas_time.axes_time.grid()
#             self.cursor = Cursor(self.plot_time.canvas_time.axes_time, useblit=True, color='k', linewidth=1)
#             self.plot_t1t2()
#             self.plot_time.canvas_time.draw()

            tmp = pd.read_excel(os.path.join(script_dir,"Supplements\Position_microphones.xlsx"),header=None)
            self.Scale_Up = tmp.iloc[0,3]

            self.Aphi = (tmp.iloc[3:,3].values).astype('float64')
            self.Athe = (tmp.iloc[3:,4].values).astype('float64')
            self.Ar = self.Scale_Up*(tmp.iloc[3:,2].values).astype('float64')

            self.Nbmic = len(self.Aphi)

            # self.in_f1.setMaximum(np.round(self.fs/2)-2)
            # self.in_f2.setMaximum(np.round(self.fs/2)-1)
            return self.fs, self.sig
        else:
            # self.open_button.setStyleSheet("background-color: red")
            pass

    def tracer(self):

        self.reinit_bouton()

        if 'fs' not in dir(self):
            self.infoBox.exec()

        elif self.t1c>=self.t2c:
            self.infoBox2.exec()
        else:

            c0 = 343

            if self.in_f1.value()>=self.in_f2.value():
                self.infoBox3.exec()
                self.in_f2.setValue(self.in_f1.value()+1)

            f1 = self.in_f1.value()
            f2 = self.in_f2.value()

            Nfft = self.fs

            # Coordonnées de l'antenne en dregrés

            Ax = self.Ar*np.cos(np.deg2rad(self.Athe))*np.cos(np.deg2rad(self.Aphi))
            Ay = self.Ar*np.cos(np.deg2rad(self.Athe))*np.sin(np.deg2rad(self.Aphi))
            Az = self.Ar*np.sin(np.deg2rad(self.Athe))

            comb = np.array(list(combinations(np.arange(self.Nbmic), 2)))

            # Scan zone

            phi = np.atleast_2d(np.arange(-180,181,1))
            the = np.atleast_2d(np.arange(-90,91,1))
            Nobs = np.size(phi,1)*np.size(the,1)

            gridx = np.reshape(np.transpose(np.cos(np.deg2rad(the)))*np.cos(np.deg2rad(phi)),Nobs)
            gridy = np.reshape(np.transpose(np.cos(np.deg2rad(the)))*np.sin(np.deg2rad(phi)),Nobs)
            gridz = np.reshape(np.transpose(np.sin(np.deg2rad(the)))*np.ones((1,np.size(phi,1))),Nobs)

            # Source

            P = self.sig[:,int(self.in_t1.value()*self.fs):int((self.in_t1.value()+self.in_t2.value())*self.fs)]

            # Filtrage des signaux

            freq = np.concatenate((np.atleast_2d(np.arange(0,self.fs/2,1)),np.atleast_2d(np.arange(self.fs/2,0,-1))),axis=1)

            r_A = (12194**2)*(freq**4)/((freq**2+20.6**2)*((freq**2+107.7**2)*(freq**2+737.9**2))**(0.5)*(freq**2+12194**2))
            r_A_1000 = (12194**2)*(1000**4)/((1000**2+20.6**2)*((1000**2+107.7**2)*(1000**2+737.9**2))**(0.5)*(1000**2+12194**2))
            r_A = r_A/r_A_1000


            # math.floor(Ls)

            signal_gl = np.zeros((self.Nbmic,np.size(P,1)))
            b, a = signal.butter(2,np.array([f1,f2])/self.fs*2,btype='bandpass')

            for imic1 in np.arange(self.Nbmic):
                 signal_gl[imic1,:] = signal.filtfilt(b, a, np.atleast_2d(P[imic1,:]))

            fft_pp = np.zeros((self.Nbmic,Nfft),dtype=complex)
            Pp = np.zeros((self.Nbmic,Nfft))
            for uu in np.arange(self.Nbmic):
               if self.pondA.isChecked():
                    fft_pp[uu,:] = ff.fft(np.atleast_2d(signal_gl[uu,:]),n=Nfft)*r_A
               else:
                    fft_pp[uu,:] = ff.fft(np.atleast_2d(signal_gl[uu,:]),n=Nfft)

               Pp[uu,:] = np.real(ff.ifft(fft_pp[uu,:]))

            Cxx2_gl = np.zeros((np.size(comb,0),Nobs))
            for imic in np.arange(np.size(comb,0)):
                 dist_E = (Ax[comb[imic,0]]*gridx)+(Ay[comb[imic,0]]*gridy)+(Az[comb[imic,0]]*gridz)
                 dist_R = (Ax[comb[imic,1]]*gridx)+(Ay[comb[imic,1]]*gridy)+(Az[comb[imic,1]]*gridz)
                 Tau = (dist_E-dist_R)/c0*self.fs

                 Ncorr = math.floor(np.max(np.abs(Tau)))+1
                 lag = np.arange(-Ncorr-1,Ncorr+1,1)

                 fE = np.atleast_2d(fft_pp[comb[imic,0],:])
                 fR = np.atleast_2d(fft_pp[comb[imic,1],:])

                 cC2 = np.real(ff.ifft(fE*np.conj(fR)))
                 Rpm = (1/Nfft)*np.concatenate((cC2[0,np.size(cC2,1)-Ncorr-1:],cC2[0,:Ncorr+1]))

                 Cxx2_gl[imic,:] = np.atleast_2d(np.interp(Tau,lag,Rpm))

            out_bf = np.mean(Cxx2_gl,axis=0)
            out_bf[out_bf<0]=0

            outp = np.reshape(10*np.log10(out_bf/4e-10),(np.size(the,1),np.size(phi,1)))
            outp_max = 10*np.log10(np.max(out_bf/4e-10))

            cc2 = 0
            cc1 = -self.ech_plot.value()

            self.plot_bf.canvas.axes.clear()
            self.plot_bf.canvas.axes.pcolormesh(np.reshape(phi,np.size(phi,1)),np.reshape(the,np.size(the,1)),outp-outp_max,cmap=plt.cm.hot_r,vmin=cc1, vmax=cc2,shading='gouraud')
            if self.pondA.isChecked():
                self.plot_bf.canvas.axes.set_title(str(np.round(outp_max,decimals=1))+" dBA")
            else:
                self.plot_bf.canvas.axes.set_title(str(np.round(outp_max,decimals=1))+" dB")

            self.plot_bf.canvas.axes.set_xlabel('$\phi$')
            self.plot_bf.canvas.axes.set_ylabel(r'$\theta$')
            self.plot_bf.canvas.draw()

class plot_bf(QtWidgets.QWidget):

    def __init__(self, parent = None):

        QtWidgets.QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure(tight_layout=True))
        vertical_layout = QtWidgets.QVBoxLayout()
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

        self.layout().addWidget(self.toolbar)
        self.layout().addWidget(self.canvas)

class plot_time(QtWidgets.QWidget):

    def __init__(self, parent = None):

        QtWidgets.QWidget.__init__(self, parent)

        self.canvas_time = FigureCanvas(Figure(tight_layout=True))
        vertical_layout = QtWidgets.QVBoxLayout()
        self.toolbar_time = NavigationToolbar(self.canvas_time, self)
        self.canvas_time.axes_time = self.canvas_time.figure.add_subplot(111)
        self.setLayout(vertical_layout)

        self.layout().addWidget(self.toolbar_time)
        self.layout().addWidget(self.canvas_time)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setQuitOnLastWindowClosed(True)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

