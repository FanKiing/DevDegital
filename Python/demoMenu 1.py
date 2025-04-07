from tkinter import *
fen=Tk()
fen.geometry("400x300")
#Etape 1 => création de la barre des menus
menuBar=Menu(fen)
#Etape 2 => création des menus principaux
menuFichier=Menu(menuBar)
#Etap 3 => Ajouter les menus principaux a la barre des menus
menuBar.add_cascade(label="Liste Emp",menu=menuFichier)
#Etape 4 Ajouter des commandes au menu pricipal
menuFichier.add_command(label="Ajouter")
menuFichier.add_command(label="Supprimer")
menuFichier.add_command(label="Quitter",command=quit)

fen.config(menu=menuBar)
fen.mainloop()