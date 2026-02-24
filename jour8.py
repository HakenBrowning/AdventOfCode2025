jonctions = []

with open('Inputs/Jour8.txt', 'r') as file:
    for line in file:
        coordonnees = list(map(int, line.strip().split(",")))
        jonctions.append(coordonnees)

# Calcul d'une distance entre 2 points dans un espace en 3D
def calculDistance(point1, point2):
    distance = 0
    for axe in range(len(point1)):
        distance += (point1[axe] - point2[axe]) ** 2
    return distance

def supprDoubles(liste):
    listeSansDouble = []
    for x in range(len(liste)):
        listeCoordonnees = []
        [listeCoordonnees.append(coord) for coord in liste[x] if coord not in listeCoordonnees]
        listeSansDouble.append(listeCoordonnees)
    return listeSansDouble
    
# Fusion des listes ayant 1 élément en commun
def fusionListe(liste):
    listeIndex = []
    elementsFusionnes = False    
    for x in range(len(liste)):
        i = 1
        while x + i < len(liste):
            if (x + i) < len(liste) and not set(liste[x]).isdisjoint(liste[x + i]):
                #print(f"Fusion détectée de {liste[x]} et {liste[x + i]} sur les éléments {set(liste[x]).intersection(liste[x + i])}")
                [liste[x].append(item) for item in liste[x + i] if item not in liste[x]]
                #print(f"Situation après : {liste[x]}")
                listeIndex.append(x + i)
                elementsFusionnes = True
            i += 1
    
    for index in listeIndex:
        liste[index] = []

    if elementsFusionnes == True:
        return fusionListe(liste)        
    else:
        return liste

# Calcul des connexions avec le nombre de connexiosn en paramètre
def connecterJonctions(liste, nbConnexions):
    positions = []
    for n in range(len(liste)):
        k = 1
        while n + k < len(liste):
            distance = calculDistance(liste[n], liste[n + k])
            positions.append([distance, n, n + k])
            k += 1
    positionsTriees = sorted(positions, key=lambda x: x[0])
    # Jusqu'ici ça semble OK
    i = 0
    connexions = []
    indexRestants = [i for i in range(len(jonctions))]
    boucleUniqueFaite = False
    while i < nbConnexions and not boucleUniqueFaite:
        print(f"Décompte : {i}")
        j = 0
        position = positionsTriees[i]
        point1 = position[1]
        point2 = position[2]
        if point1 in indexRestants:
            indexRestants.remove(point1)
        if point2 in indexRestants:
            indexRestants.remove(point2)
        estDansListe = False
        while j < len(connexions):
            if point1 in connexions[j]:
                if point2 not in connexions[j]:
                    connexions[j].append(point2)
                    estDansListe = True
                else:
                    estDansListe = True
            elif point2 in connexions[j]:
                if point1 not in connexions[j]:
                    connexions[j].append(point1)
                    estDansListe = True
                else:
                    estDansListe = True
            j += 1
        if estDansListe == False:
            connexions.append([point1, point2])
        
        connexions = fusionListe(connexions)
        connexions = [el for el in connexions if len(el) > 0]
        
        if len(connexions) == 1 and i > 1 and len(indexRestants) == 0:
            print(f"Multiplication partie 2 : {liste[point1][0] * liste[point2][0]} avec les points {liste[point1]} et {liste[point2]} et longueur {position[0]}")
            boucleUniqueFaite = True
        i += 1
    
    return supprDoubles(connexions)

#Ligne solution démo
#connexions = sorted(connecterJonctions(jonctions, 10), key=len, reverse=True)

#Lignes partie 1
#connexions = sorted(connecterJonctions(jonctions, 1000), key=len, reverse=True)
#print(f"Total = {len(connexions[0])} * {len(connexions[1])} * {len(connexions[2])} = {len(connexions[0])*len(connexions[1])*len(connexions[2])}")

#Ligne partie 2
connexions = sorted(connecterJonctions(jonctions, 10000), key=len, reverse=True)