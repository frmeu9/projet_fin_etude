import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2
from goprocam import GoProCamera
from goprocam import constants
import time



class selectFileFromCamera(tk.Frame):
    def __init__(self, window, fileListe, **kwargs):
        tk.Frame.__init__(self, window, width=1025, height=1025, **kwargs)
        # labelMainFrame = tk.Label(self, text="Logiciel")
        #         # labelMainFrame.pack()
        self.pack()

        self.fileListe = fileListe

        self.listMedia = tk.Listbox(self)
        for i in self.fileListe:
            self.listMedia.insert(tk.END, i)
        self.listMedia.pack()

        self.buttonSelect = tk.Button(self, text="Select", command=self.okButton)
        self.buttonSelect.pack()

        self.buttonClose = tk.Button(self, text="Close", command=self.quit)
        self.buttonClose.pack()

    def okButton(self):
        cameraFileInfo = self.listMedia.get(tk.ACTIVE)
        return cameraFileInfo


class downloadFile(tk.Frame):
    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width=1025, height=1025, **kwargs)
        self.pack()

        self.buttonGetFileFromComputer = tk.Button(self, text="Get file from computer", command=self.getFileFromComputer)
        self.buttonGetFileFromComputer.pack(fill=tk.X)

        self.buttonGetFileFromCamera = tk.Button(self, text="Get file from Camera", command=self.getFileFromCamera)
        self.buttonGetFileFromCamera.pack(fill=tk.X)

        self.buttonGetNoiseFile = tk.Button(self, text="Get noise file from computer", command=self.getNoiseFile)
        self.buttonGetNoiseFile.pack(fill=tk.X)

        self.buttonClose = tk.Button(self, text='Close', command=self.quit)
        self.buttonClose.pack(fill=tk.X)

        self.computerFilePath = " "
        self.img = []

    def getFileFromComputer(self):
        self.computerFilePath = tk.filedialog.askopenfilename()
        return self.computerFilePath

    def getFileFromCamera(self):
        try:
            gpCam = GoProCamera.GoPro(constants.auth)
            fileList = gpCam.listMedia(True, True)
            gpCam.mode("1")

            mini = selectFileFromCamera(tk.Tk(), fileList)
            cameraFile = mini.okButton()
            mini.mainloop()
            mini.quit()

            folder = cameraFile[0]
            file = cameraFile[1]
            time.sleep(8)
            self.img = gpCam.downloadMedia(folder, file)

            return self.img

        except AttributeError:
            self.getFileFromComputer()

    def getNoiseFile(self):
        pass


class MainFrame(tk.Frame):
    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width=1025, height=1025, **kwargs)
        self.pack()

        " Création des widgets "
        self.buttonDownloadData = tk.Button(self, text="Download files", command=self.downloadFiles)
        self.buttonDownloadData.pack(fill=tk.X)

        self.buttonSuperposition = tk.Button(self, text="Superposition", command=self.superposition)
        self.buttonSuperposition.pack(fill=tk.X)

        self.buttonRefresh = tk.Button(self, text="Refresh", command=self.changeColorMap)
        self.buttonRefresh.pack(fill=tk.X)

        self.buttonSaveAs = tk.Button(self, text="Save As", command=self.saveAs)
        self.buttonSaveAs.pack(fill=tk.X)

        self.buttonCancelMainFrame = tk.Button(self, text='Close', command=self.quit)
        self.buttonCancelMainFrame.pack(fill=tk.X)

        self.colormapChoice = tk.StringVar()
        self.choiceViridis = tk.Radiobutton(self, text='Viridis', variable=self.colormapChoice, value='viridis')
        self.choiceViridis.pack()
        self.choiceMagma = tk.Radiobutton(self, text='Magma', variable=self.colormapChoice, value='magma')
        self.choiceMagma.pack()
        self.choiceCividis = tk.Radiobutton(self, text='Cividis', variable=self.colormapChoice, value='cividis')
        self.choiceCividis.pack()

        " DATA "
        self.img = []
        self.noise = []
        self.finalImage = []

        self.computerFilePath = " "

    def downloadFiles(self):
        download = downloadFile(tk.Tk())

        download.mainloop()
        download.quit()


        self.computerFilePath = download.computerFilePath
        self.img = download.img

        print(self.computerFilePath)

    def showImage(self):
        if self.img==[]:
            self.img = cv2.imread(self.computerFilePath)
            cv2.imshow('Chosen Image', self.img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            cv2.imshow('Chosen Image', self.img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def changeColorMap(self):
        print(self.colormapChoice.get())

    def superposition(self):
        pass

    def saveAs(self):
        pass


interface = MainFrame(tk.Tk())
interface.mainloop()
interface.destroy()
