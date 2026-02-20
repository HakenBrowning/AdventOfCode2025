# Partie 1
liste_entrees = []

with open('Inputs/Jour6.txt', 'r') as file:
    for line in file:
        rangee = line.split()
        liste_entrees.append(rangee)

total = 0
nombre_calculs = len(liste_entrees[0])
indice_signes = len(liste_entrees) - 1
for num_calcul in range(0,nombre_calculs):
    calcul_intermediaire = 0
    if liste_entrees[indice_signes][num_calcul] == "+":
        for indice_ligne in range(0,indice_signes):
            calcul_intermediaire += int(liste_entrees[indice_ligne][num_calcul])
    else:
        calcul_intermediaire = 1
        for indice_ligne in range(0,indice_signes):
            calcul_intermediaire = calcul_intermediaire * int(liste_entrees[indice_ligne][num_calcul])
    total += calcul_intermediaire

print(f"Total = {total}")

# Partie 2
liste_entrees = []

with open('Inputs/Jour6.txt', 'r') as file:
    for line in file:
        liste_entrees.append(line)

colonnes_tournees = list(map(list, zip(*liste_entrees)))

#On a une liste de listes de caractères par colonne, faut maintenant trouver comment les assembler et les traiter comme il faut
indice_debut = 0
indice_fin = 0
longueur_liste = len(colonnes_tournees)
longueur_element = len(colonnes_tournees[0])
total = 0
while (indice_debut <= longueur_liste):
    colonne_blanche_trouvee = False
    while (not colonne_blanche_trouvee) and indice_fin < longueur_liste:
        est_colonne_vide = True
        for char in colonnes_tournees[indice_fin]:
            if str(char).strip() != '':
                est_colonne_vide = False
        if not est_colonne_vide:
            indice_fin += 1
        else:
            colonne_blanche_trouvee = True

    # Ici on a donc trouvé la colonne vide, donc les colonnes précédentes font partie des calculs !
    nb_occurences = indice_fin - indice_debut
    # On sauvegarde le signe dans le premier tableau, puis on re-cast
    signe = colonnes_tournees[indice_debut][longueur_element - 1]
    colonnes_tournees[indice_debut][longueur_element - 1] = ''

    resultat_inter = 0
    if signe == '*':
        resultat_inter = 1
    for colonne in range(indice_debut, indice_fin):
        if signe == '+':
            resultat_inter += int(''.join(colonnes_tournees[colonne]).strip())
        else:
            resultat_inter = resultat_inter * int(''.join(colonnes_tournees[colonne]).strip())
    total += resultat_inter
    indice_fin += 1
    indice_debut = indice_fin

print(f"Total partie 2 = {total}")


    