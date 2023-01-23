#Ce fichier sert a executer pour realiser une partie
from noyau import jouer_tour, est_pair, creer_grille, valider_contrat, total_grille, est_bonus
from affichage import afficher_grille, bienvenue, votre_main, vos_contrats, tour_joueur_1, tour_joueur_2, victoire_joueur_1, victoire_joueur_2, egalite, total
from time import sleep



main_joueur_1 = [0, 0, 0, 0, 0] #Définit la liste de la main du joueur numéro 1
main_joueur_2 = [0, 0, 0, 0, 0] #Définit la liste de la main du joueur numéro 2
mains_joueurs = []

grille_joueur_1 = creer_grille() #Créé et définit la grille du joueur numéro 1
grille_joueur_2 = creer_grille() #Créé et définit la grille du joueur numéro 2
grilles_joueurs = 0

relance = [0, 0, 0, 0, 0]
nb_tours = 0



bienvenue()

nb_joueurs = input("Choisissez le nombre de joueurs (1 ou 2) : ") #Demande le nombre de joueurs qui jouent (1 ou 2)
while nb_joueurs != "1" and nb_joueurs != "2":
    nb_joueurs = input("Choisissez le nombre de joueurs (1 ou 2) : ")

nb_joueurs = int(nb_joueurs) #Convertit en entier le choix du nombre de joueurs

while nb_tours != 13 * nb_joueurs: #Tant que le nombre de tours est différent de 13 fois le nombre de joueurs,
    if nb_joueurs == 1: #Si il y a 1 joueur,
        nb_tours = nb_tours + 1 
        mains_joueurs = main_joueur_1 #La liste "mains_joueurs" prend la valeur de la liste de la main du joueur numéro 1
        grilles_joueurs = grille_joueur_1 #La variable "grilles_joueurs" prend la valeur de la grille du joueur numéro 1
    elif nb_joueurs == 2: #Sinon si il y a 2 joueurs,
        nb_tours = nb_tours + 1
        if est_pair(nb_tours) == False: #Si le nombre de tours de jeu est impair
            mains_joueurs = main_joueur_1 #La liste "mains_joueurs" prend la valeur de la liste de la main du joueur numéro 1
            grilles_joueurs = grille_joueur_1 #La variable "grilles_joueurs" prend la valeur de la grille du joueur numéro 1
            tour_joueur_1()
        else: #Sinon
            mains_joueurs = main_joueur_2 #La liste "mains_joueurs" prend la valeur de la liste de la main du joueur numéro 2
            grilles_joueurs = grille_joueur_2 #La variable "grilles_joueurs" prend la valeur de la grille du joueur numéro 2
            tour_joueur_2()

    votre_main()
    jouer_tour(mains_joueurs, relance, grilles_joueurs) #Permet de joueur 1 tour
    sleep(2)
    vos_contrats()
    afficher_grille(grilles_joueurs) #Affiche la grille du joueur qui joue
    print()
    valider_contrat(grilles_joueurs, mains_joueurs) #Permet de valider un contrat
    print()
    afficher_grille(grilles_joueurs) #Ré-affiche la grille avec le contrat validé
    sleep(2)
    main_joueur_1 = [0, 0, 0, 0, 0] #Re-définit la liste de la main du joueur numéro 1 pour pouvoir relancer les dés au tour suivant
    main_joueur_2 = [0, 0, 0, 0, 0] #Re-définit la liste de la main du joueur numéro 2 pour pouvoir relancer les dés au tour suivant



total_joueur_1 = total_grille(grille_joueur_1) #Calcule le total de la grille du joueur 1
total_joueur_2 = total_grille(grille_joueur_2) #Calcule le total de la grille du joueur 2



if est_bonus(grille_joueur_1): #Si le total des 6 premiers contrats du joueur numéro 1 permet de donner un bonus,
    total_joueur_1 = total_joueur_1 + 35 #On rajoute le bonus au total du joueur numéro 1
if est_bonus(grille_joueur_2): #Si le total des 6 premiers contrats du joueur numéro 2 permet de donner un bonus,
    total_joueur_2 = total_joueur_2 + 35 #On rajoute le bonus au total du joueur numéro 2

if nb_joueurs == 1: #Si il y a 1 joueur,
    total()
    print("Votre total est de :", total_joueur_1) #Affiche le total du joueur numéro 1
    print()
else: #Sinon,
    if total_joueur_1 > total_joueur_2: #Si le joueur numéro 1 a plus de points,
        victoire_joueur_1() #Victoire du joueur numéro 1
    elif total_joueur_2 > total_joueur_1: #Sinon si le joueur numéro 2 a plus de points,
        victoire_joueur_2() #Victoire du joueur numéro 2
    else: #Sinon,
        egalite() #Il y a égalité
    sleep(2)
    total()
    print("Le total du joueur 1 est :", total_joueur_1) #Affiche le total du joueur numéro 1
    print()
    print("Le total du joueur 2 est :", total_joueur_2) #Affiche le total du joueur numéro 2

print("Bravo !!! N'hésitez pas à rejouer quand vous voulez.")