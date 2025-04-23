nombres = input("Entrez une liste de nombres ")

liste = nombres.split(',')
# split() est une méthode utilisée avec les chaine de caracteres(str) pour diviser une chaine en plusieurs morceaux, à
# partir d'un séparateur (comme une virgule, un espace,etc)

liste_entiers = []
for n in liste:
    if n.strip().isdigit():
        liste_entiers.append(int(n.strip()))
    else:
        raise SystemExit("Fin du programme : la liste contient des valeurs non numériques.")

somme = sum(liste_entiers)
print("Somme :", somme)

moyenne = somme / len(liste_entiers)
print("Moyenne :", round(moyenne, 2))

superieurs = [n for n in liste_entiers if n > moyenne]
print("Nombres supérieurs à la moyenne :", len(superieurs))