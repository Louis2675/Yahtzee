#Ce fichier contient les modules de gestion des sorties (affichage du programme), il contient la ou les procedures d'affichage
from noyau import *

L = [1, 2, 3, 4, 5]

def afficher_des(L):
    print("Votre main est : | ", end="")
    for i in range(len(L)):
        print(L[i], end=" | ")

afficher_des(L)