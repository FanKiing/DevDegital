from abc import ABC , abstractmethod
from datetime import datetime, timedelta

class Plante(ABC):
    def __init__(self, nom, type_plante, derniere_irrigation):
        self.nom = nom
        self.type_plante = type_plante
        self.derniere_irrigation = datetime.strptime(derniere_irrigation, '%Y-%m-%d')
        self.besoin_irrigation = False

    @abstractmethod
    def detecter_besoin_irrigation(self):
        pass

class Fleur(Plante):
    def __init__(self, nom, derniere_irrigation):
        super().__init__(nom, "Fleur", derniere_irrigation)

    def detecter_besoin_irrigation(self):
        if datetime.now() - self.derniere_irrigation > timedelta(days=7):
            self.besoin_irrigation = True
        else :
            self.besoin_irrigation = False

class Arbre(Plante):
    def __init__(self, nom, derniere_irrigation, hauteur):
        super().__init__(nom, "Arbre", derniere_irrigation)
        self.hauteur = hauteur

    def detecter_besoin_irrigation(self):
        interval = 15 if self.hauteur < 2 else 30
        if datetime.now() - self.derniere_irrigation > timedelta(days=interval):
            self.besoin_irrigation = True
        else :
            self.besoin_irrigation = False

class Cactus(Plante):
    def __init__(self, nom, derniere_irrigation, resistance_secheresse):
        super().__init__(nom, "Cactus", derniere_irrigation)
        self.resistance_secheresse = resistance_secheresse

    def detecter_besoin_irrigation(self):
        interval = 30 if self.resistance_secheresse > 5 else 30
        if datetime.now() - self.derniere_irrigation > timedelta(days=interval):
            self.besoin_irrigation = True
        else :
            self.besoin_irrigation = False

class Pepiniere :
    def __init__(self):
        self.plantes = []

    def ajouter_plante(self ,plante):
        self.plantes.append(plante)

    def verifier_irrigation(self):
        besoins = []
        for plante in self.plantes:
            plante.detecter_besoin_irrigation()
            if plante.besoin_irrigation:
                besoins.append(plante.nom)
        return besoins
    

    


if __name__ == "__main__":
    pepiniere = Pepiniere()

    fleur = Fleur("Rose", "2025-01-10")
    arbre = Arbre("Chêne", "2024-12-25", 3)
    cactus = Cactus("Saguaro", "2024-11-01", 8)

    pepiniere.ajouter_plante(fleur)
    pepiniere.ajouter_plante(arbre)
    pepiniere.ajouter_plante(cactus)

    plantes_besoin_irrigation = pepiniere.verifier_irrigation()
    print("Plantes nécessitant une irrigation :", plantes_besoin_irrigation)