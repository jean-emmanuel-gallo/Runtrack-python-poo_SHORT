class Student:
    def __init__(self, nom, prénom, numétudiant=0, level=None):
        self.__nom = nom 
        self.__prénom = prénom
        self.__numétudiant = numétudiant
        self.__crédits = 0
        self.__level = level

    def add_credits(self, credits):
        if credits > 0:
            self.__crédits += credits
        else:
            print("Le nombre de crédits doit être supérieur à zéro.")

    def studentEval(self, niveau):
      if self.__level is not None:
        if niveau >= 90:
            print("Excellent !")
        elif niveau >= 80:
            print("Très bien !")
        elif niveau >= 70:
            print("Bien")
        elif niveau >= 60:
            print("Passable")
        elif niveau > 60:
            print("Insuffisant")

    def studentInfo(self):
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prénom}")
        print(f"id: {self.__numétudiant}")
        if self.__level is not None:
            if self.__level >= 90:
                print("Niveau: Excellent !")
            elif self.__level >= 80:
                print("Niveau: Très bien !")
            elif self.__level >= 70:
                print("Niveau: Bien")
            elif self.__level >= 60:
                print("Niveau: Passable")
            else:
                print("Niveau: Insuffisant")
        else:
            print("Niveau: Non défini")
            

    def get_total_credits(self):
        return self.__crédits

    def get_nom(self):
        return self.__nom

    def get_prénom(self):
        return self.__prénom

    def get_numétudiant(self):
        return self.__numétudiant

    def get_level(self):
        return self.__level


étudiant1 = Student("Doe", "John", 145, 75)
étudiant1.add_credits(10)
étudiant1.add_credits(10)
étudiant1.add_credits(10)
print("Le total de crédits de l'étudiant", étudiant1.get_nom(), étudiant1.get_prénom(), "est de", étudiant1.get_total_credits())


étudiant1.studentEval(85)
étudiant1.studentInfo()