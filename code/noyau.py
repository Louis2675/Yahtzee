#Ce fichier sert a contenir les fonctions et procedures necessaires pour le bon fonctionnement du jeu.
from random import randint
from saisie import choisir_des, choisir_contrat
from affichage import afficher_des, afficher_grille

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

def jouer_tour(main, relance): #Procedure qui permet de realiser trois lancers / tours
    cpteur = 1
    while cpteur <= 3:  #Trois lancers
        if cpteur == 1: 
            relance = [0,0,0,0,0] # Premier lancer, pas de relances dispoibles, tous les des sont donc lances 
            lancer_des(main, relance)
            afficher_des(main)
            cpteur += 1
        if cpteur == 2 or cpteur == 3:
            relance = choisir_des()
            if relance == [0,0,0,0,0]: # Si aucune relance 
                relance = [2,2,2,2,2] # Mise des relances a 2 pour ne pas relancer la totalité des dés
            lancer_des(main, relance)
            afficher_des(main)
            cpteur += 1
       
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

# grille = creer_grille()
# afficher_grille(grille)

# choisir_contrat(grille)

def somme_totale(main): # Realise la somme des dés de la main
    total = 0
    for i in range(0, len(main)):
        total = total + main[i]
    return total

main =  [3, 3, 3, 3, 3]

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
    est_brelan = False
    cpt = [0, 0, 0, 0, 0, 0]
    for i in range(0, 5):
        cpt[main[i] - 1] = cpt[main[i] - 1] + 1 # Assigner le nombre de fois qu'un nombre est assigne
    for k in range(0, 5): 
        if cpt[k] >= 4: # Verifier si une des valeurs est brelan
            est_brelan = True
    return est_brelan

def est_yahtzee(main):
    est_brelan = False
    cpt = [0, 0, 0, 0, 0, 0]
    for i in range(0, 5):
        cpt[main[i] - 1] = cpt[main[i] - 1] + 1 # Assigner le nombre de fois qu'un nombre est assigne
    for k in range(0, 5): 
        if cpt[k] >= 5: # Verifier si une des valeurs est brelan
            est_brelan = True
    return est_brelan

print("est_brelan : ",est_brelan(main))
print("est_carre : ",est_carre(main))
print("est_yahtzee : ",est_yahtzee(main))