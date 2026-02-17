# Partie 1
total_joltage = 0

with open('Inputs/Jour3.txt', 'r') as file:
    for line in file:
        liste_line = list(line)
        valeur_max_1 = max(liste_line)
        index_max_1 = liste_line.index(valeur_max_1)

        # Soit le max est en unité, soit en dizaine
        liste_dizaines = line[0:index_max_1]
        liste_unites = line[index_max_1 + 1:]

        valeur_max_dizaines = "0"
        valeur_max_unites = "0"
        if len(liste_dizaines) > 0:
            valeur_max_dizaines = max(liste_dizaines)
        if len(liste_unites) > 0:
            valeur_max_unites = max(liste_unites)

        joltage_1 = int(valeur_max_dizaines + valeur_max_1)
        joltage_2 = int(valeur_max_1 + valeur_max_unites)

        total_joltage += max(joltage_1, joltage_2)

print(f"Total = {total_joltage}")

# Partie 2
total_joltage = 0

with open('Inputs/Jour3.txt', 'r') as file:
    for line in file:
        joltage_string = ""
        valeurs_restantes = list(line.rstrip())
        for etape in range(0,12):
            taille_liste = len(valeurs_restantes)
            valeurs_considerees = valeurs_restantes[:taille_liste - (12 - etape) + 1]
            joltage_string += max(valeurs_considerees)
            index_joltage_string = valeurs_restantes.index(max(valeurs_considerees))
            valeurs_restantes = valeurs_restantes[index_joltage_string + 1:]
        #print(f"Joltage étape = {joltage_string}")
        total_joltage += int(joltage_string)

print(f"Total partie 2 = {total_joltage}")