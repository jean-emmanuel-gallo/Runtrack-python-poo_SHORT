class Personne():
    def __init__(self, âge=14):
        self._âge = âge

    def get_âge(self):
        return self._âge

    def afficherAge(self):
        print("Vous avez", self._âge, "ans")


eleve = Personne()
eleve.afficherAge()

print("Tu as", eleve.get_âge(), "ans")

class Eleve(Personne):
    def __init__(self, âge):
        Personne.__init__(self, âge)

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai", self._âge, "ans")


class Professeur():
    def __init__(self, matièreEnseignée):
        self.__matièreEnseignée = matièreEnseignée
    
    def enseigner(self):
        print("Le cours va commencer")


élève1 = Eleve(18)
print("J'ai", élève1.get_âge(), "ans")

élève1.allerEnCours()
élève1.afficherAge()

professeur1 = Professeur("Mathématiques")
professeur1.enseigner()
