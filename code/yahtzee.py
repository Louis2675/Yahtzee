#Ce fichier sert a executer pour realiser une partie
from noyau import jouer_tour, est_pair, creer_grille, valider_contrat, total_grille, est_bonus
from affichage import afficher_grille, bienvenue, votre_main, vos_contrats, tour_joueur_1, tour_joueur_2, victoire_joueur_1, victoire_joueur_2, egalite, total



main_joueur_1 = [0, 0, 0, 0, 0]
main_joueur_2 = [0, 0, 0, 0, 0]
mains_joueurs = []

grille_joueur_1 = creer_grille()
grille_joueur_2 = creer_grille()
grilles_joueurs = 0

relance = [0, 0, 0, 0, 0]
nb_tours = 0



bienvenue()

nb_joueurs = int(input("Choisissez le nombre de joueurs (1 ou 2) : "))
while nb_joueurs != 1 and nb_joueurs != 2:
    nb_joueurs = int(input("Choisissez le nombre de joueurs (1 ou 2) : "))

while nb_tours != 13 * nb_joueurs:
    if nb_joueurs == 1:
        nb_tours = nb_tours + 1
        mains_joueurs = main_joueur_1
        grilles_joueurs = grille_joueur_1
    elif nb_joueurs == 2:
        nb_tours = nb_tours + 1
        if est_pair(nb_tours) == False:
            mains_joueurs = main_joueur_1
            grilles_joueurs = grille_joueur_1
            tour_joueur_1()
        else:
            mains_joueurs = main_joueur_2  
            grilles_joueurs = grille_joueur_2
            tour_joueur_2()

    votre_main()
    jouer_tour(mains_joueurs, relance)
    vos_contrats()
    afficher_grille(grilles_joueurs)
    print()
    valider_contrat(grilles_joueurs, mains_joueurs)
    print()
    afficher_grille(grilles_joueurs)
    main_joueur_1 = [0, 0, 0, 0, 0]
    main_joueur_2 = [0, 0, 0, 0, 0]



total_joueur_1 = total_grille(grille_joueur_1)
total_joueur_2 = total_grille(grille_joueur_2)



if est_bonus(grille_joueur_1):
    total_joueur_1 = total_joueur_1 + 35
if est_bonus(grille_joueur_2):
    total_joueur_2 = total_joueur_2 + 35

if nb_joueurs == 1:
    total()
    print("Votre total est de :", total_joueur_1)
    print()
else:
    total()
    print("Le total du joueur 1 est :", total_joueur_1)
    print()
    print("Le total du joueur 2 est :", total_joueur_2)
    if total_joueur_1 > total_joueur_2:
        victoire_joueur_1()
    elif total_joueur_2 > total_joueur_1:
        victoire_joueur_2()
    else:
        egalite()

print("Bravo !!! N'hésitez pas à rejouer quand vous voulez.")