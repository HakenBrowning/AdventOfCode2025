# Partie 1 et 2

liste_marqueurs = []
liste_rayons = []
symbole_debut = "S"
symbole_splitter = "^"
decompte_splitter_touches = 0

with open('Inputs/Jour7.txt', 'r') as file:
    for line in file:
        rangee = list(line.strip())
        liste_marqueurs.append(rangee)

for i in range(0, len(liste_marqueurs[0])):
    liste_rayons.append(0)

for ligne in range(0, len(liste_marqueurs)):
    for id in range(0, len(liste_marqueurs[ligne])):
        if liste_marqueurs[ligne][id] == symbole_debut:
            liste_rayons[id] = 1
        if liste_marqueurs[ligne][id] == symbole_splitter and liste_rayons[id] >= 1:
            decompte_splitter_touches += 1
            if id > 0:
                liste_rayons[id - 1] += liste_rayons[id]
            if id < len(liste_marqueurs[ligne]) - 1:
                liste_rayons[id + 1] += liste_rayons[id]
            liste_rayons[id] = 0

total = 0
for valeur_rayon in range(0, len(liste_rayons)):
    total += liste_rayons[valeur_rayon]

print(f"Nombre de splitters touchés = {decompte_splitter_touches}, nombre de rayons = {total}")