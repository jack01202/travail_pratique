# En python le switch case devient match case
fruits = "Pomme"
match fruits:
    case "Pomme": 
        print("J'aime les pommes")
    case "banane":
        print("je n'aime pas les banane")
    case "orange":
        print("les oranges sont bonnes pour la santé")
    case _:
        print("je ne connais pas le fruits")
   