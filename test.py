' FICHIER POUR TESTS '

import tkinter as tk
from tkinter import filedialog
import cv2
import goprocam



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
