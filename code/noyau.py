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
    return grille



def somme_totale(main): # Realise la somme des dés de la main
    total = 0
    for i in range(0, len(main)):
        total = total + main[i]
    return total



def somme_valeur(main, n):
    somme_valeur = 0    
    for i in range(0, 5):
        if main[i] == n:
            somme_valeur = somme_valeur + n
    return somme_valeur



def est_brelan(main):
    brelan = False
    cpt = [0, 0, 0, 0, 0, 0]
    for i in range(0, 5):
        cpt[main[i] - 1] = cpt[main[i] - 1] + 1 # Assigner le nombre de fois qu'un nombre est assigne
    for k in range(0, 5): 
        if cpt[k] >= 3: # Verifier si une des valeurs est brelan
            brelan = True
    return brelan



def est_carre(main):
    carre = False
    cpt = [0, 0, 0, 0, 0, 0]
    for i in range(0, 5):
        cpt[main[i] - 1] = cpt[main[i] - 1] + 1 # Assigner le nombre de fois qu'un nombre est assigne
    for k in range(0, 5): 
        if cpt[k] >= 4: # Verifier si une des valeurs est brelan
            carre = True
    return carre



def est_full(main):
    full = False
    cpt = [0, 0, 0, 0, 0, 0]
    compteur = [0, 0]
    for i in range(0, 5):
        cpt[main[i] - 1] = cpt[main[i] - 1] + 1
    for j in range(0, 5):
        if cpt[j] == 3:
            compteur[0] = 1
        if cpt[j] == 2:
            compteur[1] = 1
        if cpt[j] == 5:
            compteur[0] = 1
            compteur[1] = 1
    if compteur == [1, 1]:
        full = True
    return full



def est_petite_suite(main):
    trier_des(main)
    k = 1
    j = 2
    while k < 4: # Pour les quatres premiers dés
        if main[k] - 1 == main[k - 1]: # Si element precedent vaut valeur element actuel moins 1 
            petite_suite = True
            k = k + 1 # Verifier l'element suivant
        else: 
            petite_suite = False
            k = 4 # Stopper, forcement pas une suite
    if petite_suite == True:
            return petite_suite
    else:
        while j < 5: # Ainsi, on fait de meme pour les quatres derniers dés
            if main[j] - 1 == main[j - 1]:
                petite_suite = True
                j = j + 1
            else:
                petite_suite = False
                j = 5  
    return petite_suite



def est_grande_suite(main):
    trier_des(main)
    k = 1
    while k < 5: # Pour toute la main
        if main[k] - 1 == main[k - 1]: # Si element precedent vaut valeur element actuel moins 1
            grande_suite = True
            k = k + 1 # On verifie pour le prochain element 
        else: 
            grande_suite = False
            k = 5 # Stopper, forcement pas une liste
    return grande_suite



def est_yahtzee(main):
    yahtzee = False
    cpt = [0, 0, 0, 0, 0, 0]
    for i in range(0, 5):
        cpt[main[i] - 1] = cpt[main[i] - 1] + 1 # Assigner le nombre de fois qu'un nombre est assigne
    for k in range(0, 5): 
        if cpt[k] >= 5: # Verifier si une des valeurs est brelan
            yahtzee = True
    return yahtzee

grille = creer_grille()

main = [1,2,3,2,6]
def valider_contrat(grille, main):
    contrat = choisir_contrat(grille)
    if contrat == "brelan":
        brelan = est_brelan(main)
        if brelan == True:
            grille["brelan"] = somme_totale(main)
        else: grille["brelan"] = 0
    if contrat == "carré":
        carre = est_carre(main)
        if carre == True:
            grille["carré"] = somme_totale(main)
        else: grille["carré"] = 0
    if contrat == "full":
        full = est_full(main)
        if full == True:
            grille["full"] = 25
        else: grille["full"] = 0
    if contrat == "petite suite":
        petite_suite = est_petite_suite(main)
        if petite_suite == True:
            grille["petite suite"] = 30
        else: grille["petite suite"] = 0
    if contrat == "grande suite":
        grande_suite = est_grande_suite(main)
        if grande_suite == True:
            grille["grande suite"] = 40
        else: grille["grande suite"] = 0
    if contrat == "yahtzee":
        yahtzee = est_yahtzee(main)
        if yahtzee == True:
            grille["yahtzee"] = 50
        else: grille["yahtzee"] = 0
    if contrat == "chance":
        grille["chance"] = somme_totale(main)
    for i in range(1, 7):
        if contrat == str(i):
            grille[str(i)] = somme_valeur(main, i)
    return grille
    

grille = valider_contrat(grille, main)
afficher_grille(grille)

