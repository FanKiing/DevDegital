#tp1
'''class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher_informations(self):
        return f"Nom : {self.nom}, Age : {self.age} ans"

personne1 = Personne("Yasser", 21)
personne2 = Personne("Ahmed", 31)

print(personne1.afficher_informations())
print(personne2.afficher_informations())'''

#tp2

'''class CompteBancaire:
    taux_interet = 0.05

    def __init__(self, solde):
        self.solde = solde
    @classmethod
    def modifier_taux(clas, taux):
        clas.taux_interet = taux

    def calculer_interet_annuel(self):
        return self.solde * self.taux_interet

compte1 = CompteBancaire(2000)
compte2 = CompteBancaire(10000)

print(f"Compte 1 : {compte1.calculer_interet_annuel()}")
print(f"Compte 2 : {compte2.calculer_interet_annuel()}")

CompteBancaire.modifier_taux(0.03)

print(f"Compte 1 : {compte1.calculer_interet_annuel()}")
print(f"Compte 2 : {compte2.calculer_interet_annuel()}")
'''

#tp3

'''class CompteBancaire:
    taux_interet = 0.05  

    def __init__(self, solde):
        self.solde = solde

    @staticmethod
    def calculer_interet(solde):
        return solde * CompteBancaire.taux_interet

solde_test = 8000
interet = CompteBancaire.calculer_interet(solde_test)
print(f"L'intérêt pour un solde de {solde_test} est de {interet}")'''

#tp4

"""class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"Nom: {self.nom}, Âge: {self.age}"

    def __repr__(self):
        return f"Personne(nom='{self.nom}', age={self.age})"

personne1 = Personne("Bob", 25)
personne2 = Personne("Reda", 30)

print(str(personne1)) 
print(repr(personne1)) 

print(str(personne2))  
print(repr(personne2))  
"""

#tp5

'''class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def surface(self):
        return self.longueur * self.largeur

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.surface() == other.surface()
        return False

rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(2, 10)

print(rectangle1 == rectangle2)  '''

#tp6

'''class Animal:
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        return "Woof!"

class Chat(Animal):
    def parler(self):
        return "Meow!"

def faire_parler(animal):
    print(animal.parler())

chien = Chien()
chat = Chat()

faire_parler(chien)
faire_parler(chat)'''

#tp7

class Voiture:
    def __init__(self, vitesse_max):
        self.__vitesse_max = vitesse_max

    def get_vitesse_max(self):
        return self.__vitesse_max

    def set_vitesse_max(self, nouvelle_vitesse_max):
        if nouvelle_vitesse_max > 0:
            self.__vitesse_max = nouvelle_vitesse_max
        else:
            print("La vitesse maximale doit être supérieure à 0.")

ma_voiture = Voiture(200)

print("Vitesse maximale initiale : ", ma_voiture.get_vitesse_max())

ma_voiture.set_vitesse_max(250)

print("Nouvelle vitesse maximale : ", ma_voiture.get_vitesse_max())

ma_voiture.set_vitesse_max(-100)




