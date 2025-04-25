class Appareil:
    def __init__(self, signe, nom):
        self.__signe = signe 
        self.nom = nom
        self.__consommation = 0  # Privé

    # parametre pour l'ID
    def get_id(self):
        return self.__signe

    # parametre pour la consommation
    def set_consommation(self, valeur):
        if valeur >= 0:
            self.__consommation = valeur
        else:
            print("Erreur: La consommation ne peut pas être négative.")

    # parametre pour la consommation
    def get_consommation(self):
        return self.__consommation

# utilisation
if __name__ == "__main__":
    lampe = Appareil(2, "Lampe LED")
    lampe.set_consommation(50)
    print(f"{lampe.nom} - ID: {lampe.get_id()}, Consommation: {lampe.get_consommation()}W")
