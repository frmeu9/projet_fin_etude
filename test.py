" FICHIER POUR DES TESTS "

import tkinter as tk
from tkinter import filedialog

import lib.goprocam

# Pour aller chercher une fichier, l'ouvrir et print le contenu
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

f = open(file_path)
contents =f.read()
print(contents)

