class Livre:
    def __init__(self, titre, auteur, nbpages):
        self.__titre = titre 
        self.__auteur = auteur
        self.__nbpages = nbpages
        self.__disponible = True
    
    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nbpages(self):
        return self.__nbpages 

    def set_nbpages(self, nbpages):
        self.__nbpages = nbpages

    def verification(self):
        if self.__disponible:
            return True 
        else:
            return False 

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté !")
        else:
            print("Le livre n'est plus disponible à l'emprunt !")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu !")
        else: 
            print("Le livre n'est pas emprunté, il est donc disponible à l'emprunt !")

livre = Livre("Naruto", "Masashi Kishimoto", 321)

print("Titre : {}".format(livre.get_titre()))
print("Auteur : {}".format(livre.get_auteur()))
print("Nombre de pages :{}".format(livre.get_nbpages()))


print("Le livre est disponible", livre.verification())

livre.emprunter()

print("Le livre est disponible :", livre.verification())


livre.rendre()

print("Le livre est disponible :", livre.verification())