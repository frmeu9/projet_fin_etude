' FICHIER POUR TESTS '
#
# import tkinter
# from tkinter import *
# from tkinter import filedialog
# import cv2
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# from numpy import array, arange, sin, pi

##########################################
# Pour aller chercher un fichier.txt, l'ouvrir et print le contenu
# def getFile():
#     root = tk.Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfilename()
#     return file_path
#
# # Pour afficher une image
# def show_img():
#     file_path = getFile()
#     img = cv2.imread(file_path)
#     cv2.imshow('image',img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#######################
# from goprocam import GoProCamera
# from goprocam import constants
# import time
# gpCam = GoProCamera.GoPro(constants.auth)
# gpCam.overview()
# gpCam.listMedia(True)


#########################

# class Interface(Frame):
#     """Notre fenêtre principale.
#     Tous les widgets sont stockés comme attributs de cette fenêtre."""
#
#     def __init__(self, fenetre, **kwargs):
#         Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
#         self.pack(fill=BOTH)
#         self.nb_clic = 0
#
#         # Création de nos widgets
#         self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
#         self.message.pack()
#
#         self.bouton_GetFile = Button(self, text="Get File", command=self.getFile)
#         self.bouton_GetFile.pack()
#
#         self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
#         self.bouton_quitter.pack(side="left")
#
#         self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red", command=self.cliquer)
#         self.bouton_cliquer.pack(side="right")
#
#     def getFile(self):
#         file_path = filedialog.askopenfilename()
#         return file_path
#
#     def cliquer(self):
#         """Il y a eu un clic sur le bouton.
#
#         On change la valeur du label message."""
#
#         self.nb_clic += 1
#         self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)
#
# fenetre = Tk()
# interface = Interface(fenetre)
# interface.mainloop()
# interface.destroy()

#############################
# root = Tk()
# frame = Frame(root)
# image = PhotoImage(file='C:/Users/Stagiaire/Desktop/Stage/Projet_fin_etude/noiseradar.PNG')
# button = Button(frame, image=image)
# button.pack()
# frame.pack()
# root.mainloop()

###############################

# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# import cv2
# from goprocam import GoProCamera
# from goprocam import constants
# import time
#
#
#
# class selectFileFromCamera:
#     def __init__(self, master, fileListe):
#         self.master = master
#         master.title("Select file in")
#
#         self.fileListe = fileListe
#
#         self.listMedia = tk.Listbox(master)
#         for i in self.fileListe:
#             self.listMedia.insert(tk.END, i)
#         self.listMedia.pack()
#
#         self.buttonSelect = tk.Button(master, text="Select", command=self.okButton)
#         self.buttonSelect.pack()
#
#         self.buttonClose = tk.Button(master, text="Close", command=self.master.quit)
#         self.buttonClose.pack()
#
#     def okButton(self):
#         cameraFileInfo = self.listMedia.get(tk.ACTIVE)
#         return cameraFileInfo
#
#
# class downloadFile:
#     def __init__(self, master):
#         self.master = master
#         master.title("Download")
#
#         self.buttonGetFileFromComputer = tk.Button(master, text="Get file from computer",
#         command=self.getFileFromComputer)
#         self.buttonGetFileFromComputer.pack(fill=tk.X)
#
#         self.buttonGetFileFromCamera = tk.Button(master, text="Get file from Camera", command=self.getFileFromCamera)
#         self.buttonGetFileFromCamera.pack(fill=tk.X)
#
#         self.buttonGetNoiseFile = tk.Button(master, text="Get noise file from computer", command=self.getNoiseFile)
#         self.buttonGetNoiseFile.pack(fill=tk.X)
#
#         self.buttonClose = tk.Button(master, text='Close', command=self.master.quit)
#         self.buttonClose.pack(fill=tk.X)
#
#         self.computerFilePath = " "
#         self.img = []
#
#     def getFileFromComputer(self):
#         self.computerFilePath = tk.filedialog.askopenfilename()
#         return self.computerFilePath
#
#     def getFileFromCamera(self):
#         try:
#             gpCam = GoProCamera.GoPro(constants.auth)
#             fileList = gpCam.listMedia(True, True)
#             gpCam.mode("1")
#
#             root3 = tk.Tk()
#             selectFileCamera = selectFileFromCamera(root3, fileList)
#             cameraFile = selectFileCamera.okButton()
#             root3.mainloop()
#             root3.destroy()
#
#             folder = cameraFile[0]
#             file = cameraFile[1]
#             time.sleep(8)
#             self.img = gpCam.downloadMedia(folder, file)
#
#             return self.img
#
#         except AttributeError:
#             self.getFileFromComputer()
#
#     def getNoiseFile(self):
#         pass
#
#
# class MainFrame:
#     def __init__(self, master):
#         self.master = master
#         master.title("Logiciel")
#         master.minsize(300,300)
#
#         " Création des widgets "
#         self.buttonDownloadData = tk.Button(master, text="Download files", command=self.downloadFiles)
#         self.buttonDownloadData.pack(fill=tk.X)
#
#         self.buttonSuperposition = tk.Button(master, text="Superposition", command=self.superposition)
#         self.buttonSuperposition.pack(fill=tk.X)
#
#         self.buttonRefresh = tk.Button(master, text="Refresh", command=self.changeColorMap)
#         self.buttonRefresh.pack(fill=tk.X)
#
#         self.buttonSaveAs = tk.Button(master, text="Save As", command=self.saveAs)
#         self.buttonSaveAs.pack(fill=tk.X)
#
#         self.buttonCancelMainFrame = tk.Button(master, text='Close', command=self.master.quit)
#         self.buttonCancelMainFrame.pack(fill=tk.X)
#
#         self.colormapChoice = tk.StringVar()
#         self.choiceViridis = tk.Radiobutton(master, text='Viridis', variable=self.colormapChoice, value='viridis')
#         self.choiceViridis.pack()
#         self.choiceMagma = tk.Radiobutton(master, text='Magma', variable=self.colormapChoice, value='magma')
#         self.choiceMagma.pack()
#         self.choiceCividis = tk.Radiobutton(master, text='Cividis', variable=self.colormapChoice, value='cividis')
#         self.choiceCividis.pack()
#
#         " DATA "
#         self.img = []
#         self.noise = []
#         self.finalImage = []
#
#         self.computerFilePath = " "
#
#     def downloadFiles(self):
#         root2 = tk.Tk()
#         downloadFrame = downloadFile(root2)
#         root2.mainloop()
#         root2.destroy()
#
#
#         self.computerFilePath = downloadFrame.computerFilePath
#         self.img = downloadFrame.img
#
#         print(self.computerFilePath)
#
#     def showImage(self):
#         if self.img==[]:
#             self.img = cv2.imread(self.computerFilePath)
#             cv2.imshow('Chosen Image', self.img)
#             cv2.waitKey(0)
#             cv2.destroyAllWindows()
#         else:
#             cv2.imshow('Chosen Image', self.img)
#             cv2.waitKey(0)
#             cv2.destroyAllWindows()
#
#     def changeColorMap(self):
#         print(self.colormapChoice.get())
#
#     def superposition(self):
#         pass
#
#     def saveAs(self):
#         pass
#
#
# root = tk.Tk()
# interface = MainFrame(root)
# root.mainloop()
# root.destroy()
############################################
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# from matplotlib.colors import ListedColormap
#
# import numpy as np
#
# image = mpimg.imread("C:/Users/meuni/Desktop/ÉCOLE/UNI/Session A4/
# Projet de fin d'étude/projet_fin_etude/src/image/softdb.png")
# print(image)
#
# plt.imshow(image, cmap="viridis")
# plt.show()
#########################################################
# Python program for blending of
# images using OpenCV

# import OpenCV file
# import cv2
#
# _, src, dst = perspective_transform(image, corners)
# Minv = cv2.getPerspectiveTransform(dst, src)
#
# # Create an image to draw the lines on
# warp_zero = np.zeros_like(image[:, :, 0]).astype(np.uint8)
# color_warp = np.dstack((warp_zero, warp_zero, warp_zero))
#
# # Recast the x and y points into usable format for cv2.fillPoly()
# pts = np.vstack((fitx, ploty)).astype(np.int32).T
#
# # Draw the lane onto the warped blank image
# # plt.plot(left_fitx, ploty, color='yellow')
# cv2.polylines(color_warp, [pts], False, (0, 255, 0), 10)
# # cv2.fillPoly(color_warp, np.int_([pts]), (0, 255, 0))
#
# # Warp the blank back to original image space using inverse perspective matrix (Minv)
# newwarp = cv2.warpPerspective(color_warp, Minv, (image.shape[1], image.shape[0]))
#
# # Combine the result with the original image
# result = cv2.addWeighted(image, 1, newwarp, 0.3, 0)
############################################################################################
# import sys
# import time
#
# import numpy as np
#
# from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
# if is_pyqt5():
#     from matplotlib.backends.backend_qt5agg import (
#         FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
# else:
#     from matplotlib.backends.backend_qt4agg import (
#         FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
# from matplotlib.figure import Figure
#
#
# class ApplicationWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self._main = QtWidgets.QWidget()
#         self.setCentralWidget(self._main)
#         layout = QtWidgets.QVBoxLayout(self._main)
#
#         static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
#         layout.addWidget(static_canvas)
#         self.addToolBar(NavigationToolbar(static_canvas, self))
#
#         dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
#         layout.addWidget(dynamic_canvas)
#         self.addToolBar(QtCore.Qt.BottomToolBarArea,
#                         NavigationToolbar(dynamic_canvas, self))
#
#         self._static_ax = static_canvas.figure.subplots()
#         t = np.linspace(0, 10, 501)
#         self._static_ax.plot(t, np.tan(t), ".")
#
#         self._dynamic_ax = dynamic_canvas.figure.subplots()
#         self._timer = dynamic_canvas.new_timer(
#             100, [(self._update_canvas, (), {})])
#         self._timer.start()
#
#     def _update_canvas(self):
#         self._dynamic_ax.clear()
#         t = np.linspace(0, 10, 101)
#         # Shift the sinusoid as a function of time.
#         self._dynamic_ax.plot(t, np.sin(t + time.time()))
#         self._dynamic_ax.figure.canvas.draw()
#
#
# if __name__ == "__main__":
#     qapp = QtWidgets.QApplication(sys.argv)
#     app = ApplicationWindow()
#     app.show()
#     qapp.exec_()
#########################################################################################################################
import matplotlib.pyplot as plt
import re
angle = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80', '85', '90',
 '95', '100', '105', '110', '115', '120', '125', '130', '135', '140', '145', '150', '155', '160', '165', '170', '175', '180',
 '185', '190', '195', '200', '205', '210', '215', '220', '225', '230', '235', '240', '245', '250', '255', '260', '265',
 '270', '275', '280', '285', '290', '295', '300', '305', '310', '315', '320', '325', '330', '335', '340', '345', '350', '355']

noise = ['2,344911E-9', '2,394874E-9', '2,443849E-9', '2,461865E-9', '2,454746E-9', '2,400632E-9', '2,329486E-9',
 '2,270706E-9', '2,213696E-9', '2,167525E-9', '2,131667E-9', '2,104676E-9', '2,085574E-9', '2,078431E-9', '2,081977E-9',
 '2,097991E-9', '2,126019E-9', '2,168823E-9', '2,234748E-9', '2,271227E-9', '2,302079E-9', '2,295351E-9', '2,296223E-9',
 '2,313133E-9', '2,322944E-9', '2,285312E-9', '2,239045E-9', '2,197718E-9', '2,172958E-9', '2,162947E-9', '2,166810E-9',
 '2,181686E-9', '2,212798E-9', '2,256796E-9', '2,317660E-9', '2,385254E-9', '2,457013E-9', '2,523050E-9', '2,557685E-9',
 '2,574982E-9', '2,527942E-9', '2,472196E-9', '2,395653E-9', '2,338517E-9', '2,282957E-9', '2,240279E-9', '2,204209E-9',
 '2,177967E-9', '2,159014E-9', '2,144998E-9', '2,137425E-9', '2,135534E-9', '2,144636E-9', '2,165617E-9', '2,197930E-9',
 '2,238379E-9', '2,285497E-9', '2,334890E-9', '2,379353E-9', '2,361550E-9', '2,309228E-9', '2,255983E-9', '2,215893E-9',
 '2,189504E-9', '2,175088E-9', '2,170557E-9', '2,174410E-9', '2,179887E-9', '2,190837E-9', '2,210654E-9', '2,241688E-9',
 '2,286977E-9']

for i in range(len(angle)):
    angle[i] = float(angle[i])
    noise[i] = re.sub(',', '.', noise[i])
    noise[i] = float(noise[i])

fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
ax1.plot(angle, noise)
ax2.plot(angle, noise)

plt.show()