position = 50 #Maximum 99, à 100 il redevient 0
nb_zero = 0
nb_passages_zero = 0

#Partie 1
with open('Inputs/Jour1.txt', 'r') as file:
    for line in file:
        lettre = line[0]
        incr = int(line[1:])

        #On ajoute ou soustrait selon la lettre
        if lettre.upper() == 'L':
            position = position - incr
        else:
            position = position + incr

        #Si modulo différent : on repasse par 0
        position = position % 100
        if position == 0:
            nb_zero += 1      

print(f"Nombre de 0 en résultat : {nb_zero}")

# Partie 2 - solution sale
position = 50 #Maximum 99, à 100 il redevient 0
nb_zero = 0
with open('Inputs/Jour1.txt', 'r') as file:
    for line in file:
        lettre = line[0]
        incr = int(line[1:])

        for i in range(incr):
            if lettre.upper() == "L":
                position -= 1
            else:
                position += 1

            if position % 100 == 0:
                nb_zero += 1

print(f"Nombre de 0 en résultat : {nb_zero}")