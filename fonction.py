# une fanction sans parametre
"""def afficher_message():
    print ("Bonjour, comment tu va ?")
afficher_message()"""

#fonction avec parametre
"""def afficher_nom_prenom(nom,prenom):
    print("Nom : ", nom)
    print ("Prenom : ", prenom)
afficher_nom_prenom("Dupont" , "Jean")"""

#fonction avec une valeur de retour
def calculer_somme(a,b) :
    resultat = a + b
    return resultat
sommes = calculer_somme(20,30)
print(sommes)