class Appareil:
    def afficher_type(self):
        print("Ceci est un appareil générique.")

class LumiereConnectee(Appareil):
    def afficher_type(self):  # Redéfinition
        print("Ceci est une lumière connectée.")

class Ventilateur(Appareil):
    def afficher_type(self):  
        print("Ceci est un ventilateur intelligent.")

# utilisation
if __name__ == "__main__":
    appareils = [Appareil(), LumiereConnectee(), Ventilateur()]
    for appareil in appareils:
        appareil.afficher_type()  
