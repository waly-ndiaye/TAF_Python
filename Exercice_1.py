# Déclaration des classes
class Table:

    def __init__(self,referance, matiere, poids, hauteur, longueur, largeur, prixVen, PrixFabri):
        self.referance=referance
        self.matiere= matiere
        self.poids= poids
        self.hauteur= hauteur
        self.longueur= longueur
        self.largeur= largeur
        self.prixDeVente= prixVen
        self.__prixDeFabrication= PrixFabri
        self.__nombreDeTableEnStock = 80

    def getPrixDeFabrication(self):
        return self.__prixDeFabrication

    def setPrixDeFabrication(self, NouvelleValeur):
        self.__prixDeFabrication = NouvelleValeur

    def getNombreDeTableEnStock(self):
        return self.__nombreDeTableEnStock

    def setNombreDeTableEnStock(self, NouvelleValeur):
        self.__nombreDeTableEnStock = NouvelleValeur

    def afficherInformation(self):
        print(f"""
        la référence = {self.referance}
        la matière de la table = {self.matiere}
        la longueur x largeur x hauteur (cm) = {self.longueur} {self.largeur} {self.hauteur}cm
        le poids de la table = {self.poids}kg
        le prix de vente = {self.prixDeVente}FCFA
        """)
    # Une méthode de calcul de gain prévu par rapport au stock.
    def calculDeGain(self):
        print("Gain= ", (self.prixDeVente-self.__prixDeFabrication)*self.__nombreDeTableEnStock)
        

# Programme Principal
table1 = Table(referance="A36B", matiere="Bois", poids=50, hauteur=20, longueur=100, largeur=30, prixVen=15000, PrixFabri=10000)
table2 = Table(referance="BN51D4", matiere="Or", poids=200, hauteur=40, longueur=50, largeur=20, prixVen=200000, PrixFabri=95000)

table1.afficherInformation()
table2.afficherInformation()

table1.setPrixDeFabrication(5000)
print(table1.getPrixDeFabrication())

table2.calculDeGain()