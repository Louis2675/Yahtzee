#Ce fichier sert a contenir les fonctions et procedures necessaires pour le bon fonctionnement du jeu.
from random import randint
from saisie import choisir_des, choisir_contrat
from affichage import afficher_des, afficher_grille



def generer_lancer(): #Fonction qui retourne un nombre aleatoire entre 1 et 6
    return randint(1,6)



def trier_des(main): #Met les elements de la liste dans l'ordre croissant 
    for i in range(len(main)):             # boucle pour parcourir toute la liste : i donne la position (en partant de la fin) à laquelle on fait remonter "l'élément bulle"
        for j in range(len(main)-i-1):     # boucle pour remonter le plus grand élément de la sous-liste L[0:i]
            if main[j] > main[j+1]:           # on échange deux éléments consécutifs s'ils ne sont pas dans le bon ordre
                aux = main[j]
                main[j] = main[j+1]
                main[j+1] = aux



def lancer_des(main, relance):
    if main == [0, 0, 0, 0, 0]:
        for i in range(1, len(main)+1): # Attribue un nombre entre 1 et 6 pour chaque element du dictionnaire
            main[i - 1] = generer_lancer()
    if relance != [0, 0, 0, 0, 0]: # Si relance non nulle, commencer la procedure
        for j in range(1, len(relance)+1): # Attribuer un nouveau tirage si relance est non nulle
            if relance[j - 1] == 1:
                main[j - 1] = generer_lancer()



def jouer_tour(main, relance): #Procedure qui permet de realiser trois lancers / tours
    lancer = 1
    while lancer <= 3:  #Trois lancers
        if lancer == 1:
            lancer_des(main, relance)
            afficher_des(main)
        elif lancer == 2 or lancer == 3:
            choisir_des(relance)
            lancer_des(main, relance)
            afficher_des(main)
        relance = [0, 0, 0, 0, 0]
        lancer = lancer + 1



def creer_grille(): # Initialise la grille pour les contrats - par defaut aucun contrat n'est rempli. on definira la grille d'une personne avec joueur1 = creer_grille() / joueur2 = creer_grille()
    grille = {}
    for i in range(0, 6):
        grille["{}".format(i + 1)] = -1
    grille["brelan"] = -1
    grille["carré"] = -1
    grille["full"] = -1
    grille["petite suite"] = -1
    grille["grande suite"] = -1
    grille["yahtzee"] = -1
    grille["chance"] = -1



def somme_totale(main): # Realise la somme des dés de la main
    total = 0
    for i in range(0, len(main)):
        total = total + main[i]
    return total



def somme_valeur(main):
    return False



def est_brelan(main):
    est_brelan = False
    cpt = [0, 0, 0, 0, 0, 0]
    for i in range(0, 5):
        cpt[main[i] - 1] = cpt[main[i] - 1] + 1 # Assigner le nombre de fois qu'un nombre est assigne
    for k in range(0, 5): 
        if cpt[k] >= 3: # Verifier si une des valeurs est brelan
            est_brelan = True
    return est_brelan



def est_carre(main):
    est_carre = False
    cpt = [0, 0, 0, 0, 0, 0]
    for i in range(0, 5):
        cpt[main[i] - 1] = cpt[main[i] - 1] + 1 # Assigner le nombre de fois qu'un nombre est assigne
    for k in range(0, 5): 
        if cpt[k] >= 4: # Verifier si une des valeurs est brelan
            est_carre = True
    return est_carre



def est_full(main):
    est_full = False
    cpt = [0, 0, 0, 0, 0, 0]
    compteur = [0, 0]
    for i in range(0, 5):
        cpt[main[i] - 1] = cpt[main[i] - 1] + 1
    for j in range(0, 5):
        if cpt[j] == 3:
            compteur[0] = 1
        if cpt[j] == 2:
            compteur[1] = 1
    if compteur == [1, 1]:
        est_full = True
    return est_full



def est_petite_suite(main):
    cpt = [0, 0, 0, 0, 0]
    for i in range(0, 5):
        cpt[main[i] - 1] = cpt[main[i] - 1] + 1 # Assigner le nombre de fois qu'un nombre est assigne
        print(cpt)



def est_grande_suite(main):
    return False



def est_yahtzee(main):
    est_yahtzee = False
    cpt = [0, 0, 0, 0, 0, 0]
    for i in range(0, 5):
        cpt[main[i] - 1] = cpt[main[i] - 1] + 1 # Assigner le nombre de fois qu'un nombre est assigne
    for k in range(0, 5): 
        if cpt[k] >= 5: # Verifier si une des valeurs est brelan
            est_yahtzee = True
    return est_yahtzee



def valider_contrat():
    return False



main = [0, 0, 0, 0, 0]
relance = [0, 0, 0, 0, 0]