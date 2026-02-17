# Partie 1
total_erreurs = 0

with open('Inputs/Jour2.txt', 'r') as file:
    for line in file:
        plages = line.split(",")
        for plage in plages:
            bornes = plage.split("-")
            borne_inf = bornes[0]
            borne_sup = bornes[1]
            for nombre in range(int(borne_inf), int(borne_sup)):
                nombre_str = str(nombre)
                longueur_nombre = len(nombre_str)
                moitie_1 = nombre_str[0:longueur_nombre//2]
                moitie_2 = nombre_str[longueur_nombre//2:longueur_nombre]
                if moitie_1 == moitie_2:
                    total_erreurs += nombre

print(f"Total final = {total_erreurs}")

# Partie 2 - Patterns complexes
total_erreurs = 0

with open('Inputs/Jour2.txt', 'r') as file:
    for line in file:
        plages = line.split(",")
        for plage in plages:
            bornes = plage.split("-")
            borne_inf = bornes[0]
            borne_sup = bornes[1]
            for nombre in range(int(borne_inf), int(borne_sup) + 1):
                # Différence ici, on ne divise pas que par 2, il faut check tous les patterns possibles
                nombre_str = str(nombre)
                longueur_nombre = len(nombre_str) 
                limite_calcul = longueur_nombre // 2 

                pattern_trouve = False
                for mult in range(1, limite_calcul + 1): 
                    # On ne fait les calculs que si la longueur est un multiple de mult (pour économiser des boucles)
                    if longueur_nombre % mult == 0:
                        indice_base = 0
                        pattern_intermediaire = True
                        while(indice_base + 2*mult <= longueur_nombre and pattern_intermediaire):
                            partie_1 = nombre_str[indice_base:indice_base + mult]
                            partie_2 = nombre_str[indice_base + mult:indice_base + 2*mult]
                            indice_base += mult
                            pattern_intermediaire = pattern_intermediaire and partie_1 == partie_2
                            
                        if pattern_intermediaire:
                            pattern_trouve = True

                if pattern_trouve:
                    total_erreurs += nombre
                    print(f"Détecté : {nombre}, Total = {total_erreurs}")

print(f"Total final partie 2 = {total_erreurs}")