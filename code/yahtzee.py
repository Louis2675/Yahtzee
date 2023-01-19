#Ce fichier sert a executer pour realiser une partie
from noyau import jouer_tour



mains_joueurs = [1, 2]
main_joueur_1 = [0, 0, 0, 0, 0]
main_joueur_2 = [0, 0, 0, 0, 0]
relance = [0, 0, 0, 0, 0]

mains_joueurs[0] = main_joueur_1
mains_joueurs[1] = main_joueur_2



jouer_tour(mains_joueurs, relance)