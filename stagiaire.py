class Stagiare:
    def __init__(self, numi=None, age=None, nom=None, prenom=None, note1=None, note2=None):
        self.__numinscription = numi
        self.__age = age
        self.__nom = nom
        self.__prenom = prenom
        self.__note1 = note1
        self.__note2 = note2
    
    def calculMoy(self):
        moy = (self.__note1+self.__note2)/2
        print("La moyenne: ", moy)
        
    # get and set
    def getnumi(self):
        return self.__numinscription
    
    def getage(self):
        return self.__age
    
    def getnom(self):
        return self.__nom
    
    def getprenom(self):
        return self.__prenom
    
    def getnote1(self):
        return self.__note1
    
    def getnote2(self):
        return self.__note2


s1 = Stagiare(1122, 21, "elgarrai", "zineb", 15.2, 18)
s2 = Stagiare()
s2.setnumi(2211)
s2.setage(15)
s2.setnom("Alouie")
s2.setprenom("Aya")
s2.setnote1(15.2)
s2.setnote2(18)     