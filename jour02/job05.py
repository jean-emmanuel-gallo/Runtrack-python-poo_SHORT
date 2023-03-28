#Je vais copier/coller le job04 

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme): 
    def __init__(self, longueur, largeur):
        self._longueur = longueur 
        self._largeur = largeur

    def aire(self):
        return self._longueur * self._largeur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return 3.14 * self.radius ** 2


rectangle1 = Rectangle(10, 20)
rectangle1.aire()
print("L'aire du rectangle est de :", rectangle1.aire())  
cercle1 = Cercle(100)
cercle1.aire()
print("L'air du cercle est de :", cercle1.aire())
