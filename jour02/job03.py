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

    def périmètre(self):
        return 2 * (self.__longueur + self.__largeur) 


    def surface(self): 
        return self.__longueur * self.__largeur


class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        self.__longueur = longueur
        self.__largeur = largeur 
        self.__hauteur = hauteur 

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def get_hauteur(self):
        return self.__hauteur 
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.__longueur * self.__largeur * self.__hauteur



rectangle1 = Rectangle(10, 30)
rectangle1.périmètre()
rectangle1.surface()

parallélépipède1 = Parallélépipède(10, 40, 80)
parallélépipède1.volume()

print("Le périmètre de rectangle1 est de :", rectangle1.périmètre())
print("La surface de rectangle1 est de :", rectangle1.surface())

print("Le volume du  est de :", parallélépipède1.volume())