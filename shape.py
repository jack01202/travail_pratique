from abc import ABC # permet de définir des classes de base

class Shape(ABC):
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length * self.length
class Triangle (Square):
    def __init__(self, base,hauteur):
        self.base = base
        self.hauteur = hauteur
    def area1(self):
        return (self.hauteur * self.base)/2
    
class Carree (Square):
    def __init__(self, bases, hauteurs):
       self.hauteurs= hauteurs
       self.bases = bases
    def area2(self):
        return (self.hauteurs * self.bases)/2
    
surface1 = Carree (10,15)
surface1_area = surface1.area2()
print(surface1_area)

surface = Triangle(5,7)
surface_area = surface.area1()
print(surface_area)

square = Square(6)
square_area = square.area()
print(square_area)