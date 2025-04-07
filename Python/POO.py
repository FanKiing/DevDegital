#Exercice 1
class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = 0

    def demarrer(self):
        print("La voiture démarre")

    def rouler(self, kilometres):
        self.kilometrage += kilometres
        print(f"La voiture a roulé {kilometres} kilomètres. Kilométrage actuel : {self.kilometrage} kilomètres")

ma_voiture = Voiture("Peugeot", "208", 2015)

ma_voiture.demarrer()
ma_voiture.rouler(50)
ma_voiture.rouler(100)


#Exercice 2
class Voiture:
    nombre_voitures = 0
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        Voiture.nombre_voitures += 1
voiture1 = Voiture("Toyota", "Corolla")
voiture2 = Voiture("Honda", "Civic")
voiture3 = Voiture("Ford", "Focus")

print(f"Nombre total de voitures créées : {Voiture.nombre_voitures}")


#Exercice 3
