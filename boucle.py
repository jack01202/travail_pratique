#boucles 
"""
races_de_chien = ["golden retriever","chihuahua","terrier","carlin"]
for chien in races_de_chien :
    print(chien)
"""

#boucles sur la varaible nom
"""nom = "ordinateur"
for ordi in nom :
    print(ordi)"""

#fonction range
"""for nombre in range(1000) :
    print(nombre)"""
"""for x in range(10):
    print(f"{x} bouteilles de bieres au mur!")"""

# boucles while
"""capacite_maximale = 10
capacite_actuelle = 3
while capacite_actuelle < capacite_maximale :
    print (f"la capacite actuelle est {capacite_actuelle}")
    capacite_actuelle += 1 """
# utilisons mot-clés break et continue

# break
"""for i in range(10):
    if i == 110 :
        break 
    print(i)"""

# continue
liste = [1,2,3,4,5]
#Boucle for sur la liste
for element in liste:
    if element == 4:
    # si l'element vaut 3, on passe a l'iteration suivente
    # sans executer le reste du code
        continue
    # dans tous les autres cas, on execute le reste du code
    print(element)
