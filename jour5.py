# Partie 1
lecture_rangees_finie = False
liste_bornes = []
nb_produits_valides = 0

with open('Inputs/Jour5.txt', 'r') as file:
    for line in file:
        entree = line.rstrip()
        if len(entree) == 0:
            lecture_rangees_finie = True
        else:
            if lecture_rangees_finie:
                # On est dans les valeurs à vérifier, on boucle pour cela
                produit_valide = False
                verification_faite = False
                while (not produit_valide) and (not verification_faite):
                    for ingredient_range in range(0, len(liste_bornes)):
                        ingredient_id = int(entree)
                        if ingredient_id >= liste_bornes[ingredient_range][0] and ingredient_id <= liste_bornes[ingredient_range][1]:
                            produit_valide = True
                    verification_faite = True
                if produit_valide:
                    nb_produits_valides += 1
            else:
                # On a une ligne de bornes, il faut les enregistrer
                duo_bornes = entree.split("-")
                duo_bornes_int = [0,0]
                duo_bornes_int[0] = int(duo_bornes[0])
                duo_bornes_int[1] = int(duo_bornes[1])
                liste_bornes.append(duo_bornes_int)

print(f"Nombre de produits valides = {nb_produits_valides}")

# Partie 2
lecture_rangees_finie = False
liste_bornes = []

with open('Inputs/Jour5.txt', 'r') as file:
    for line in file:
        entree = line.rstrip()
        if len(entree) == 0:
            lecture_rangees_finie = True
        else:
            if not lecture_rangees_finie:
                duo_bornes = entree.split("-")
                duo_bornes_int = [0,0]
                duo_bornes_int[0] = int(duo_bornes[0])
                duo_bornes_int[1] = int(duo_bornes[1])
                liste_bornes.append(duo_bornes_int)

liste_bornes_triee = sorted(liste_bornes, key= lambda x: (x[0], x[1]))
indice_lecture = 0
nb_produits_valides = 0

while indice_lecture < len(liste_bornes_triee) - 1:
    modification_faite = False
    if liste_bornes_triee[indice_lecture][1] >= liste_bornes_triee[indice_lecture + 1][0] and liste_bornes_triee[indice_lecture][1] <= liste_bornes_triee[indice_lecture + 1][1]:
        liste_bornes_triee[indice_lecture][1] = liste_bornes_triee[indice_lecture + 1][1]
        del liste_bornes_triee[indice_lecture + 1]
        modification_faite = True
    if not modification_faite and liste_bornes_triee[indice_lecture + 1][1] >= liste_bornes_triee[indice_lecture][0] and liste_bornes_triee[indice_lecture + 1][1] <= liste_bornes_triee[indice_lecture][1]:
        del liste_bornes_triee[indice_lecture + 1]
        modification_faite = True
    if not modification_faite:
        indice_lecture += 1

for bornes in liste_bornes_triee:
    nb_produits_valides += (bornes[1] - bornes[0] + 1)


print(f"Nombre de produits valides partie 2 = {nb_produits_valides}")