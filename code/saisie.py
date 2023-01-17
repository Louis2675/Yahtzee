#Ce fichier sert a contenir le module de gestion des entrees, il contient les fonctions de saisie (protegee)

# Pour la liste relance, les indexes sont comme suivant: relance[0] = dé #0+1


def choisir_des(relance): # mise en place du systeme de relances. Un dé est relance si la valeur de son index dans le dictionnaire est egal a 1.
    sortie = False
    while sortie == False:
        a = input("Voulez-vous relancer un dé ? (non pour finir) : ")
        if a == "1" or a == "2" or a == "3" or a == "4" or a == "5":
            relance[int(a) - 1] = 1
        elif a == "non":
            sortie = True
        else:
            print("Mauvaise entrée, veuillez recommencer : ")

def choisir_contrat(grille): 
    compteur = 0 
    while compteur == 0:
        a = input("Choisissez le contrat que vous voulez remplir (Attention à chosir un contrat valide) : ")
        if a.lower() in grille.keys():
            compteur = compteur + 1         
        else:
            print("Mauvaise entrée, veuillez recommencer : ")
