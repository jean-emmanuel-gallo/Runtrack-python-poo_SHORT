class Livre:
    def __init__(self, titre, auteur, nbpages):
        self.__titre = titre 
        self.__auteur = auteur
        self.__nbpages = nbpages
    
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
        if isinstance(nbpages, int) and nbpages > 0:
            self.__nbpages = nbpages
            print("Le nombre de page est bel et bien un nombre entier !")
        else:
            print("Le nombre de pages n'est pas un nombre entier !")

livre = Livre("Naruto", "Masashi Kishimoto", 321)

print("Titre : {}".format(livre.get_titre()))
print("Auteur : {}".format(livre.get_auteur()))
print("Nombre de pages :{}".format(livre.get_nbpages()))


livre.set_titre("Naruto Shippuden")
livre.set_auteur("Masashi Kishimoto")
livre.set_nbpages(400)

print("Titre : {}".format(livre.get_titre()))
print("Auteur : {}".format(livre.get_auteur()))
print("Nombre de pages :{}".format(livre.get_nbpages()))

livre.set_nbpages(311)
livre.set_nbpages(800)
