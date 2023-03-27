class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur 
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

rectangle1 = Rectangle(10, 5)

print("La longueur initiale du rectangle est de : ", rectangle1.get_longueur())
print("La largeur initiale du rectangle est de : ", rectangle1.get_largeur())

rectangle1.set_longueur(30)
rectangle1.set_largeur(15)

print("la longueur est maintenant de :{}".format(rectangle1.get_longueur()))
print("la largeur est maintenant de :{}".format(rectangle1.get_largeur()))

