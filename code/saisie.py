#Ce fichier sert a contenir le module de gestion des entrees, il contient les fonctions de saisie (protegee)
from affichage import afficher_grille



def choisir_des(relance, grille): #Cette fonction permet de choisir les dés à relancer
    sortie = False
    while sortie == False:
        choix = input("Voulez-vous relancer un dé ? (non pour finir, grille pour afficher votre grille) : ") #Demande si on veut relancer un dé
        if choix == "1" or choix == "2" or choix == "3" or choix == "4" or choix == "5": #Si on décide de relancer un dé en donnant son numéro,
            relance[int(choix) - 1] = 1 #On change la valeur du dé dans la liste relance
        elif choix == "non": #Si le choix est non,
            sortie = True #On sort de la boucle
        elif choix == "grille": #Si le choix est grille,
            print()
            afficher_grille(grille) #On affiche la grille du joueur
            print()
        else: #Sinon,
            print("Mauvaise entrée, veuillez recommencer : ") #On redemande un choix

            
            
def choisir_contrat(grille): #Cette fonction permet de choisir le contrat qu´on veut valider
    compteur = 0 
    while compteur == 0:
        contrat = input("Choisissez le contrat que vous voulez remplir (Attention à chosir un contrat valide) : ")
        if contrat.lower() in grille.keys(): #Si le contrat choisit correspond à un contrat existant dans la grille,
            compteur = compteur + 1 #On sort de la boucle
        else: #Sinon,
            print("Mauvaise entrée, veuillez recommencer : ") #On redemande
    return contrat
