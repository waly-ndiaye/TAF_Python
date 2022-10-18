# Définition de la classe
class Pet:
    def __init__(self) -> None:
        self.__name = input("Entrer le nom de l'animal: ")
        self.__animalType = input("Entrer son Type: ")
        self.__age = input("Entrer son age: ")
    
    def petInformation(self):
        print(f"""
        nom = {self.__name}
        type = {self.__animalType}
        age= {self.__age}
        """)

# Programme Principal  
nouveauPet = Pet()
nouveauPet.petInformation()