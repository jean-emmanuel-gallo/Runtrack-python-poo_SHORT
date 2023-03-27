class Personne:
    def __init__(self, nom, prénom):
        self.nom = nom
        self.prénom = prénom

    def sePrésenter(self):
        print("Bonjour, je me nomme", self.prénom, self.nom)


personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")

personne1.sePrésenter()
personne2.sePrésenter()
