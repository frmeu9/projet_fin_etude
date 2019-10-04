' FICHIER POUR TESTS '

import tkinter
from tkinter import *
from tkinter import filedialog
import cv2
import goprocam
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from numpy import array, arange, sin, pi


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
from goprocam import GoProCamera
from goprocam import constants
import time
gpCam = GoProCamera.GoPro(constants.auth)
gpCam.overview()
gpCam.listMedia(True)


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