#Ce fichier sert a executer pour realiser une partie
from noyau import jouer_tour, est_pair, creer_grille, valider_contrat
from affichage import afficher_grille, bienvenue, votre_main, vos_contrats, tour_joueur_1, tour_joueur_2, victoire_joueur_1, victoire_joueur_2, egalite



main_joueur_1 = [0, 0, 0, 0, 0]
main_joueur_2 = [0, 0, 0, 0, 0]
mains_joueurs = []

grille_joueur_1 = creer_grille()
grille_joueur_2 = creer_grille()
grilles_joueurs = 0

relance = [0, 0, 0, 0, 0]
nb_tours = 0



bienvenue()

choix_nb_joueurs = str(input("Choisissez le nombre de joueurs (un ou deux) : "))
while choix_nb_joueurs != "un" and choix_nb_joueurs != "deux":
    choix_nb_joueurs = str(input("Choisissez le nombre de joueurs (un ou deux) : "))

if choix_nb_joueurs == "un":
    tour_joueur_1()
    while nb_tours != 13:
        nb_tours = nb_tours + 1
        mains_joueurs = main_joueur_1
        grilles_joueurs = grille_joueur_1

        votre_main()
        jouer_tour(mains_joueurs, relance)
        vos_contrats()
        afficher_grille(grilles_joueurs)
        print()
        valider_contrat(grilles_joueurs, mains_joueurs)
        print()
        afficher_grille(grilles_joueurs)
        main_joueur_1 = [0, 0, 0, 0, 0]

if choix_nb_joueurs == "deux":
    while nb_tours != 26:
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

#Tout ce qui est avant ce commentaire fonctionne et est bon. Il reste juste ce que j'ai mis en bas à faire.

total_joueur_1 = 11  #Faire le total de la grille du joueur numéro 1
total_joueur_2 = 11  #Faire le total de la grille du joueur numéro 2

#Faire que si le total des 6 premiers contrats est supérieur ou égal à 63, on ajoute 35 points à total_joueur_1/2

if total_joueur_1 > total_joueur_2:
    victoire_joueur_1()
elif total_joueur_2 > total_joueur_1:
    victoire_joueur_2()
else:
    egalite()

#Régler le problème de "est_full" qui renvoie que 0 dans la grille (alors qu'il marche si on le teste indépendamment)
#À voir si il y a également d'autre fonctions qui renvoient 0 dans la grille (je ne les ai pas toutes testées)