# Étape 1 : Demande des deux nombres
nombre1 = input("Entrez le premier nombre : ")
nombre2 = input("Entrez le deuxième nombre : ")

# Étape 2 : Vérification que ce sont bien des nombres
if not nombre1.isnumeric() or not nombre2.isnumeric():
    raise SystemExit("Fin du programme : les deux valeurs doivent être des nombres.")

# Étape 4 : Conversion en entiers
nombre1 = int(nombre1)
nombre2 = int(nombre2)

# Étape 5 : Demande de l'opération
operation = input("Entrez une opération (+, -, *, /) : ")

# Étape 6 : Vérification de l'opération
if operation not in ['+', '-', '*', '/']:
    raise SystemExit("Fin du programme : opération non valide.")

# Étape 7-8 : Calcul avec condition pour la division par zéro
if operation == '+':
    resultat = nombre1 + nombre2
elif operation == '-':
    resultat = nombre1 - nombre2
elif operation == '*':
    resultat = nombre1 * nombre2
elif operation == '/':
    if nombre2 == 0:
        raise SystemExit("Fin du programme : division par zéro interdite.")
    resultat = round(nombre1 / nombre2, 2)
    
# Étape 10 : Affichage
print("Le résultat est :", resultat)