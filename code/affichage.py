#Ce fichier contient les modules de gestion des sorties (affichage du programme), il contient la ou les procedures d'affichage
from noyau import *

def afficher_des(L): # Fonction qui affiche la main du joueur 
    print('''
 _   _       _                                  _       
| | | |     | |                                (_)      
| | | | ___ | |_ _ __ ___       _ __ ___   __ _ _ _ __  
| | | |/ _ \| __| '__/ _ \     | '_ ` _ \ / _` | | '_ \ 
\ \_/ / (_) | |_| | |  __/     | | | | | | (_| | | | | |
 \___/ \___/ \__|_|  \___|     |_| |_| |_|\__,_|_|_| |_|
                                                                ''')
    print("    D1      D2      D3      D4      D5")
    print(41*"-")
    print("|   ", end="")
    for i in range(1, len(L)+1): #Prend chaque element de la main et les place dans les cases
        print(L[i - 1], end="   |   ")
    print("")
    print(41*"-")


lancer_des(main)
print(main)
afficher_des(main)

