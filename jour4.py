# Partie 1
liste_emplacements = []

# D'abord on charge toutes les lignes
with open('Inputs/Jour4.txt', 'r') as file:
    for line in file:
        rangee = list(line.rstrip())
        rangee_booleen = []
        for emplacement in range(0,len(rangee)):
            if rangee[emplacement] == '@':
                rangee_booleen.append(1)
            else:
                rangee_booleen.append(0)
        liste_emplacements.append(rangee_booleen)

# Ensuite on vérifie, pour chaque entrée valide, si ses voisins le sont aussi. Si < 4, ça compte
nombre_rouleaux_accessibles = 0
hauteur_etagere = len(liste_emplacements)
for indice_rangee in range(0,hauteur_etagere):
    longueur_rangee = len(liste_emplacements[indice_rangee])
    for indice_place in range(0,longueur_rangee):
        if liste_emplacements[indice_rangee][indice_place] == 1:
            nombre_voisins = 0
            if indice_rangee > 0 and indice_place > 0 and liste_emplacements[indice_rangee - 1][indice_place - 1] == 1:
                nombre_voisins += 1
            if indice_rangee > 0 and liste_emplacements[indice_rangee - 1][indice_place] == 1:
                nombre_voisins += 1
            if indice_rangee > 0 and indice_place < longueur_rangee - 1 and liste_emplacements[indice_rangee - 1][indice_place + 1] == 1:
                nombre_voisins += 1
            if indice_place > 0 and liste_emplacements[indice_rangee][indice_place - 1] == 1:
                nombre_voisins += 1
            if indice_place < longueur_rangee - 1 and liste_emplacements[indice_rangee][indice_place + 1] == 1:
                nombre_voisins += 1
            if indice_rangee < hauteur_etagere - 1 and indice_place > 0 and liste_emplacements[indice_rangee + 1][indice_place - 1] == 1:
                nombre_voisins += 1
            if indice_rangee < hauteur_etagere - 1 and liste_emplacements[indice_rangee + 1][indice_place] == 1:
                nombre_voisins += 1
            if indice_rangee < hauteur_etagere - 1 and indice_place < longueur_rangee - 1 and liste_emplacements[indice_rangee + 1][indice_place + 1] == 1:
                nombre_voisins += 1
            if nombre_voisins < 4:
                nombre_rouleaux_accessibles += 1

print(f"Nombre de rouleaux accessibles = {nombre_rouleaux_accessibles}")

# Partie 2
liste_emplacements = []

# D'abord on charge toutes les lignes
with open('Inputs/Jour4.txt', 'r') as file:
    for line in file:
        rangee = list(line.rstrip())
        rangee_booleen = []
        for emplacement in range(0,len(rangee)):
            if rangee[emplacement] == '@':
                rangee_booleen.append(1)
            else:
                rangee_booleen.append(0)
        liste_emplacements.append(rangee_booleen)

# Ensuite on vérifie, pour chaque entrée valide, si ses voisins le sont aussi. Si < 4, ça compte
nombre_rouleaux_accessibles = 0
nombre_rouleaux_precedemment_accessibles = -1
liste_emplacements_suivante = liste_emplacements
hauteur_etagere = len(liste_emplacements)
while (nombre_rouleaux_accessibles != nombre_rouleaux_precedemment_accessibles):
    nombre_rouleaux_precedemment_accessibles = nombre_rouleaux_accessibles
    for indice_rangee in range(0,hauteur_etagere):
        longueur_rangee = len(liste_emplacements[indice_rangee])
        for indice_place in range(0,longueur_rangee):
            if liste_emplacements[indice_rangee][indice_place] == 1:
                nombre_voisins = 0
                if indice_rangee > 0 and indice_place > 0 and liste_emplacements[indice_rangee - 1][indice_place - 1] == 1:
                    nombre_voisins += 1
                if indice_rangee > 0 and liste_emplacements[indice_rangee - 1][indice_place] == 1:
                    nombre_voisins += 1
                if indice_rangee > 0 and indice_place < longueur_rangee - 1 and liste_emplacements[indice_rangee - 1][indice_place + 1] == 1:
                    nombre_voisins += 1
                if indice_place > 0 and liste_emplacements[indice_rangee][indice_place - 1] == 1:
                    nombre_voisins += 1
                if indice_place < longueur_rangee - 1 and liste_emplacements[indice_rangee][indice_place + 1] == 1:
                    nombre_voisins += 1
                if indice_rangee < hauteur_etagere - 1 and indice_place > 0 and liste_emplacements[indice_rangee + 1][indice_place - 1] == 1:
                    nombre_voisins += 1
                if indice_rangee < hauteur_etagere - 1 and liste_emplacements[indice_rangee + 1][indice_place] == 1:
                    nombre_voisins += 1
                if indice_rangee < hauteur_etagere - 1 and indice_place < longueur_rangee - 1 and liste_emplacements[indice_rangee + 1][indice_place + 1] == 1:
                    nombre_voisins += 1
                if nombre_voisins < 4:
                    nombre_rouleaux_accessibles += 1
                    liste_emplacements_suivante[indice_rangee][indice_place] = 0
    liste_emplacements = liste_emplacements_suivante

print(f"Nombre de rouleaux nouvellement accessibles = {nombre_rouleaux_accessibles}")