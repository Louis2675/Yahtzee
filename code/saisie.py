#Ce fichier sert a contenir le module de gestion des entrees, il contient les fonctions de saisie (protegee)

def choisir_des(relance): # mise en place du systeme de relances. Un dé est relance si la valeur de son index dans le dictionnaire est egal a 1.
    sortie = False
    while sortie == False:
        choix = input("Voulez-vous relancer un dé ? (non pour finir) : ")
        if choix == "1" or choix == "2" or choix == "3" or choix == "4" or choix == "5":
            relance[int(choix) - 1] = 1
        elif choix == "non":
            sortie = True
        else:
            print("Mauvaise entrée, veuillez recommencer : ")

def choisir_contrat(grille): 
    compteur = 0 
    while compteur == 0:
        contrat = input("Choisissez le contrat que vous voulez remplir (Attention à chosir un contrat valide) : ")
        if contrat.lower() in grille.keys():
            compteur = compteur + 1         
        else:
            print("Mauvaise entrée, veuillez recommencer : ")
    return contrat