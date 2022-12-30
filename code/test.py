# relance = [0, 0, 0, 0, 0]

# if relance == [0, 0, 0, 0, 0]:
#     print("true")

# relance["d{}".format(a)] = 1
# print(relance)

# def lancer_des(main, relance):
#     cpt = 1
#     while cpt <= 3:
#         if cpt == 1:
#             for i in range(1, len(main)+1): # Attribue un nombre entre 1 et 6 pour chaque element du dictionnaire
#                 main[i - 1] = generer_lancer()
#                 print("lancer 1 realise")
#                 cpt += 1
#         if cpt == 2 or cpt == 3:
#             relance = [0, 0, 0, 0, 0]
#             relance = choisir_des(relance)
#             for i in range(1, len(relance+1)):
#                 if relance[i - 1] == 1:
#                     main[i - 1] = generer_lancer()
#             cpt += 1 