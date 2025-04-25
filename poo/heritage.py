class Appareil:
    def __init__(self, identite, nom, type):
        self._identite = identite  # Encapsulation (attribut protégé)
        self.nom = nom
        self.type = type
        self._statut = False  # Privé

    def afficher_infos(self):
        print(f"Appareil: {self.nom} (Type: {self.type}, Statut: {'Allumé' if self._statut else 'Éteint'})")

class Thermostat(Appareil):
    def __init__(self, id, nom, temperature_cible):
        super().__init__(id, nom, "Thermostat")
        self.temperature_cible = temperature_cible

    def afficher_infos(self):  # Polymorphisme (redéfinition)
        print(f"Thermostat: {self.nom}, Température cible: {self.temperature_cible}°C")

# utilisation
if __name__ == "__main__":
    thermo = Thermostat(1, "Thermo Salon", 24)
    thermo.afficher_infos()  # Affiche les infos du thermostat
