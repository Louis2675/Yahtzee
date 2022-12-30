#Ce fichier sert a contenir les fonctions et procedures necessaires pour le bon fonctionnement du jeu.
from random import randint
from saisie import choisir_des

def generer_lancer(): #Fonction qui retourne un nombre aleatoire entre 1 et 6
    return randint(1,6)

def trier_des(L): #Met les elements de la liste dans l'ordre croissant 
    for i in range(1, len(L)):
        while L[i] < L[i - 1] and i > 0:
            L[i] += L[i - 1]
            L[i - 1] = L[i] - L[i - 1]
            L[i] -= L[i - 1]
            i -= 1
    return L

main = [0, 0, 0, 0, 0]
relance = [0, 0, 0, 0, 0]

def lancer_des(main, relance): 
    for i in range(1, len(main)+1): # Attribue un nombre entre 1 et 6 pour chaque element du dictionnaire
        main[i - 1] = generer_lancer()
        if relance != [0, 0, 0, 0, 0]: 
            for k in range(1, len(relance)+1): # Attribuer un nouveau tirage si relance est non nulle
                if relance[i - 1] == 1:
                    main[i - 1] = generer_lancer()

relance = choisir_des(relance)