# Définition des classes
import code
from copy import deepcopy


class Personne:
    def __init__(self, nom, prenom, cin):
        self.nom = nom
        self.prenom = prenom
        self.cin = cin
    
    def toString(self):
        print(f"\n\tnom = {self.nom}\n\tprenom = {self.prenom}\n\tcin = {self.cin}")

class Vaccine(Personne):
    def __init__(self, nom, prenom, cin, code, date):
        super().__init__(nom, prenom, cin)
        self.___codeDeVaccination = code
        self.__dateDeVaccination = date

    def getcodeDeVaccination(self):
        return self.___codeDeVaccination
    def setcodeDeVaccination(self, code):
        self.___codeDeVaccination = code

    def getdateDeVaccination(self):
        return self.__dateDeVaccination
    def setdateDeVaccination(self, date):
        self.__dateDeVaccination = date

    def toString(self):
        super().toString()
        print(f"\tcodeDeVaccination = {self.___codeDeVaccination}\n\tDateDeVaccination = {self.__dateDeVaccination}\n\t")

class Vaccin:
    def __init__(self, cod, nom, duree) -> None:
        self.code = cod
        self.nom = nom
        self.dureeEntre2Doses = duree
    def __copyConstructor__(self, original):
        self.code = original.code
        self.nom = original.nom
        self.dureeEntre2Doses = original.dureeEntre2Doses
    def toString(self):
        print(f"\n\tnom Du Vaccin = {self.nom}\n\tCode Du Vaccin = {self.code}\n\tduree entre 2 doses = {self.dureeEntre2Doses}\n")

# Programme Principal
personne1 = Personne(nom="Fakoro", prenom="Traore", cin="25A35BC")

personne1.toString()

vaccine1 = Vaccine(nom="Papou", prenom="Keita", cin="19J1M1045Z", code=122, date="12/05/2021")
vaccine2 = Vaccine(nom="Henry", prenom="Hart", cin="00AZ4500", code=36, date="14/12/2018")

vaccine2.toString()
vaccine1.setcodeDeVaccination("002500B")
print("Code De vaccination:" , vaccine1.getcodeDeVaccination())

vaccin1 = Vaccin(cod=65, nom="Covid-Killer", duree=2)
vaccin3 = Vaccin(cod=0, nom="", duree=0)
vaccin2 = deepcopy(vaccin1)
vaccin3.__copyConstructor__(original=vaccin1)

vaccin1.toString()
vaccin2.toString()
vaccin3.toString()