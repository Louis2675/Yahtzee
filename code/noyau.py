#Ce fichier sert a contenir les fonctions et procedures necessaires pour le bon fonctionnement du jeu.
from random import randint
from saisie import choisir_des
from affichage import afficher_des

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

main = [0, 0, 0, 0, 0] #pre-def main 
relance = [0, 0, 0, 0, 0] #pre-def relance

def lancer_des(main, relance): 
    if relance == [0, 0, 0, 0, 0]:
        for i in range(1, len(main)+1): # Attribue un nombre entre 1 et 6 pour chaque element du dictionnaire
            main[i - 1] = generer_lancer()
    if relance != [0, 0, 0, 0, 0]: # Si relance non nulle, commencer la procedure
        for k in range(1, len(relance)+1): # Attribuer un nouveau tirage si relance est non nulle
            if relance[k - 1] == 1:
                main[k - 1] = generer_lancer()

def jouer_tour(main, relance): 
    cpteur = 1
    while cpteur <= 3: 
        if cpteur == 1:
            relance = [0,0,0,0,0]
            lancer_des(main, relance)
            print("Lancer 1 terminé : ")
            afficher_des(main)
            cpteur += 1
        if cpteur == 2 or cpteur == 3:
            relance = choisir_des()
            if relance == [0,0,0,0,0]:
                relance = [2,2,2,2,2]
            lancer_des(main, relance)
            afficher_des(main)
            cpteur += 1

            

jouer_tour(main, relance)
        
