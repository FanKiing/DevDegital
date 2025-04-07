#/----------Ex1------------/

from abc import ABC, abstractmethod

class Livre:
    def __init__(self, titre, auteur, annee_publication, disponible=True):
        self.__titre = titre
        self.__auteur = auteur
        self.__annee_publication = annee_publication
        self.__disponible = disponible

    def afficher_details(self):
        statut = "Disponible" if self.__disponible else "Emprunté"
        print(f"Titre: {self.__titre} , Auteur: {self.__auteur}"
              f"Année: {self.__annee_publication} , Statut: {statut}")

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_annee_publication(self):
        return self.__annee_publication

    def set_annee_publication(self, annee_publication):
        self.__annee_publication = annee_publication

    def est_disponible(self):
        return self.__disponible

    def marquer_emprunte(self):
        self.__disponible = False

    def marquer_retourne(self):
        self.__disponible = True

class Personne(ABC):
    @abstractmethod
    def afficher_detail(self):
        pass

class Utilisateur(Personne):
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.livre_empruntes = []

    def afficher_detail(self):
        print(f"Nom: {self.nom} ,Email: {self.email}")
        if self.livre_empruntes:
            print("Livre emprunté")
            for livre in self.livre_empruntes:
                print(f" - {livre.get_titre()}")
        else:
            print("Aucune livre emprunté ")

    def emprunter_livre(self, livre):
        if livre.est_disponible():
            livre.marquer_emprunte()
            self.livre_empruntes.append(livre)  
        else:
            print(f"Le livre '{livre.get_titre()} n'est pas disponible.")

class Bibliothecaire(Utilisateur):
    def __init__(self, nom, email):
        super().__init__(nom, email)
        self.livre_gestion = []

    def ajouter_livre(self, livre):
        self.livre_gestion.append(livre)
        print(f"Le livre '{livre.get_titre()}' a été ajouté à la bibliothèque.")

    def afficher_detail(self):
        super().afficher_detail()
        print("(Utilisateur est un bibliothécaire)")

if __name__ == "__main__":
    livre1 = Livre("A song of ice and fire", "George R.R Martin", 1998)
    livre2 = Livre("The lord of the rings", "J.R.R.Tolkien", 1954)

    utilisateur = Utilisateur("Yassir", "yassir@example.com")
    utilisateur.emprunter_livre(livre1)
    utilisateur.afficher_detail() 

    utilisateur = Utilisateur("Essaih", "essaih@example.com")
    utilisateur.emprunter_livre(livre2)
    utilisateur.afficher_detail()  