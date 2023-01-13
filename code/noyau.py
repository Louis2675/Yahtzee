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

def est_brelan(main):
    cpt1 = 0
    cpt2 = 0
    cpt3 = 0
    cpt4 = 0
    cpt5 = 0
    cpt6 = 0
    for i in range(0, 5):
        if main[i] == 1:
            cpt1 = cpt1 + 1
        if main[i] == 2:
            cpt2 = cpt2 + 1
        if main[i] == 3:
            cpt3 = cpt3 + 1
        if main[i] == 4:
            cpt4 = cpt4 + 1
        if main[i] == 5:
            cpt5 = cpt5 + 1
        if main[i] == 6:
            cpt6 = cpt6 + 6
    if cpt1 >= 3 or cpt2 >= 3 or cpt3 >= 3 or cpt4 >= 3 or cpt5 >= 3 or cpt6 >= 3: est_brelan = True
    else: est_brelan = False
    return est_brelan

def est_carre(main):
    cpt1 = 0
    cpt2 = 0
    cpt3 = 0
    cpt4 = 0
    cpt5 = 0
    cpt6 = 0
    for i in range(0, 5):
        if main[i] == 1:
            cpt1 = cpt1 + 1
        if main[i] == 2:
            cpt2 = cpt2 + 1
        if main[i] == 3:
            cpt3 = cpt3 + 1
        if main[i] == 4:
            cpt4 = cpt4 + 1
        if main[i] == 5:
            cpt5 = cpt5 + 1
        if main[i] == 6:
            cpt6 = cpt6 + 6
    if cpt1 >= 4 or cpt2 >= 4 or cpt3 >= 4 or cpt4 >= 4 or cpt5 >= 4 or cpt6 >= 4: est_carre = True
    else: est_carre = False
    return est_carre

def est_yahtzee(main):
    cpt1 = 0
    cpt2 = 0
    cpt3 = 0
    cpt4 = 0
    cpt5 = 0
    cpt6 = 0
    for i in range(0, 5):
        if main[i] == 1:
            cpt1 = cpt1 + 1
        if main[i] == 2:
            cpt2 = cpt2 + 1
        if main[i] == 3:
            cpt3 = cpt3 + 1
        if main[i] == 4:
            cpt4 = cpt4 + 1
        if main[i] == 5:
            cpt5 = cpt5 + 1
        if main[i] == 6:
            cpt6 = cpt6 + 6
    if cpt1 >= 5 or cpt2 >= 5 or cpt3 >= 5 or cpt4 >= 5 or cpt5 >= 5 or cpt6 >= 5: est_yahtzee = True
    else: est_yahtzee = False
    return est_yahtzee

print("est_brelan : ",est_brelan(main))
print("est_carre : ",est_carre(main))
print("est_yahtzee : ",est_yahtzee(main))