#Ce fichier sert a contenir le module de gestion des entrees, il contient les fonctions de saisie (protegee)

# Pour la liste relance, les indexes sont comme suivant: relance[0] = dé #0+1


def choisir_des(): # mise en place du systeme de relances. Un dé est relance si la valeur de son index dans le dictionnaire est egal a 1.
    relance = [0, 0, 0, 0, 0]
    cpt = 0
    while cpt == 0:
        a = input("Relancer un dé ? (non pour finir) : ")
        if a == "1" or a == "2" or a == "3" or a == "4" or a == "5":
            relance[int(a) - 1] = 1
        elif a == "non":
            cpt = 1
            return relance
        else:
            print("Mauvaise entree, veuillez recommencer.")

def choisir_contrat(grille): 
    cpt = 0 
    while cpt == 0:
        a = input("Chosir le contrat que vous voulez remplir (attention a chosir un contrat valide) : ")
        if a.lower() in grille.keys():
            cpt += 1         
        else:
            print("Entrée incorrecte, veuillez réessayer")
