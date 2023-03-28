class Véhicule():
    def __init__(self, marque, modèle, année, prix):
        self._marque = marque
        self._modèle = modèle
        self._année = année 
        self._prix = prix 

    def informationsVehicule(self):
        print(f"Marque = {self._marque}\nModèle = {self._modèle}\nAnnée = {self._année}\nPrix = {self._prix}")

class Voiture(Véhicule):
    def __init__(self, marque, modèle, année, prix, portes):
        self._marque = marque
        self._modèle = modèle 
        self._année = année 
        self._prix = prix
        self._portes = portes 

    def informationsVehicule(self):
        print(f"Marque = {self._marque}\nModèle = {self._modèle}\nAnnée = {self._année}\nPrix = {self._prix}")

    def démarrer(self):
        print("Attention, moi la voiture je roule !")

class Moto(Véhicule):
    def __init__(self, marque, modèle, année, prix, roues):
        self._marque = marque
        self._modèle = modèle 
        self._année = année 
        self._prix = prix
        self._roues = roues

    def informationsVehicule(self):
        print(f"Marque = {self._marque}\nModèle = {self._modèle}\nAnnée = {self._année}\nPrix = {self._prix}\nRoues = {self._roues}")

    def démarrer(self):
        print("Attention, moi la Moto je roule !")



bateau = Véhicule("Zodiac", "Z-2000", 1990, 12000)
bateau.informationsVehicule()

voiture1 = Voiture("Mercedes", "Class A", 2020, 18500, 4)
voiture1.informationsVehicule()
voiture1.démarrer()

moto1 = Moto("Yamaha", "1200 Vmax", 1987, 4500, 2)
moto1.informationsVehicule()
moto1.démarrer()