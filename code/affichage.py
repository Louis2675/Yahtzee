#Ce fichier contient les modules de gestion des sorties (affichage du programme), il contient la ou les procedures d'affichage


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

def afficher_grille(grille):
    print(""" 
_   _                             _             _       
| | | |                           | |           | |      
| | | | ___  ___    ___ ___  _ __ | |_ _ __ __ _| |_ ___ 
| | | |/ _ \/ __|  / __/ _ \| '_ \| __| '__/ _` | __/ __|
\ \_/ / (_) \__ \ | (_| (_) | | | | |_| | | (_| | |_\__ {} 
 \___/ \___/|___/  \___\___/|_| |_|\__|_|  \__,_|\__|___/
                                                        """.format("\\"))
    i = 0
    for key, value in grille.items():
        i += 1
        if value != -1:
            print("Contrat n° {} ({}) : {}".format(i, key, value))
        else: 
            print("Contrat n° {} ({}) :".format(i, key))