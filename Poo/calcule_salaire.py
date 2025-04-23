def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4

def salaire_horaire(salaire_hebdo, heures):
    return round(salaire_hebdo / heures, 2)

salaire_annuel = float(input("Entrez votre salaire annuel en $ : "))
heures_par_semaine = float(input("Entrez le nombre d'heures travaillées par semaine : "))
mensuel = salaire_mensuel(salaire_annuel)
hebdo = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdo, heures_par_semaine)

print(f"Votre salaire horaire est de {horaire} $.")