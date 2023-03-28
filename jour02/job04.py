class Forme:
    def aire(self):
        return 0

class Rectangle(Forme): 
    def __init__(self, longueur, largeur):
        self._longueur = longueur 
        self._largeur = largeur

    def aire(self):
        return self._longueur * self._largeur


rectangle1 = Rectangle(10, 20)
rectangle1.aire()
print("L'aire du rectangle est de :", rectangle1.aire())        