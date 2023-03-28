class Personne():
    def __init__(self, âge=14):
        self._âge = âge

    def get_âge(self):
        return self._âge

    def afficherAge(self):
        print("J'ai", self._âge, "ans")


eleve = Personne()
eleve.afficherAge()


class Eleve(Personne):
    def __init__(self, âge):
        Personne.__init__(self, âge)

    def allerEnCours(self):
        print("Je vais en cours")

    def bonjour(self):
        print("Bonjour !")


class Professeur(Personne):
    def __init__(self, matièreEnseignée, âge=40):
        Personne.__init__(self, âge)
        self.__matièreEnseignée = matièreEnseignée

    def bonjour(self):
        print("Bonjour je suis le professeur !")

    def enseigner(self):
        print("Le cours va commencer")






élève1 = Eleve(15)
élève1.allerEnCours()
élève1.afficherAge()
élève1.bonjour()

professeur1 = Professeur("Python", 40)
professeur1.bonjour()
print("J'ai", professeur1.get_âge(), "ans")
professeur1.enseigner()

