class Animal:
    def __init__(self, age, prénom):
        self.age = age
        self.prénom = prénom

    def vieillir(self):
        print("l'âge de l'animal", self.age+1, "ans")

    def nommer(self):
        print("L'animal se nomme", self.prénom)

animal1=Animal(2, "Luna")

animal1.vieillir()
animal1.nommer()

