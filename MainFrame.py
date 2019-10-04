import tkinter as tk
from tkinter import filedialog
import cv2
from goprocam import GoProCamera
from goprocam import constants

# import matplotlib as mpl
# import matplotlib.pyplot as plt


class MainFrame(tk.Frame):
    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width=1025, height=1025, **kwargs)
        self.pack()

        "Création des widgets"
        self.buttonGetFileFromComputer = tk.Button(self, text="Get file from computer", command=self.showImageFromComputer)
        self.buttonGetFileFromComputer.pack(side="top")

        self.buttonGetFileFromCamera = tk.Button(self, text="Get file from Camera", command=self.showImageFromCamera)
        self.buttonGetFileFromCamera.pack()

        self.buttonCloseMainFrame = tk.Button(self, text='Close', command=self.quit)
        self.buttonCloseMainFrame.pack()

        colormapChoice = tk.StringVar()
        choiceViridis = tk.Radiobutton(self, text='Viridis', variable=colormapChoice, value='viridis')
        choiceMagma = tk.Radiobutton(self, text='Magma', variable=colormapChoice, value='magma')
        choiceCividis = tk.Radiobutton(self, text='Cividis', variable=colormapChoice, value='cividis')
        choiceViridis.pack()
        choiceMagma.pack()
        choiceCividis.pack()

    def getFileFromComputer(self):
        file_path = tk.filedialog.askopenfilename()
        return file_path

    def showImageFromComputer(self):
        filePath = self.getFileFromComputer()
        img = cv2.imread(filePath)
        cv2.imshow('Chosen Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def showImageFromCamera(self):
        gpCam = GoProCamera.GoPro(constants.auth)
        if gpCam == 1 :
            self.showImageFromComputer()
        else:
            pass




fenetre = tk.Tk()
interface = MainFrame(fenetre)
interface.mainloop()
interface.destroy()
