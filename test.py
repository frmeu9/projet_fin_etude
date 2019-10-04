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
#         self.buttonGetFileFromComputer = tk.Button(master, text="Get file from computer", command=self.getFileFromComputer)
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
