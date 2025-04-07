from abc import ABC , abstractmethod
import json
import csv

class Document(ABC):
    def __init__(self, id, titre, auteur, annee_publication):
        if annee_publication < 1990:
            raise ValueError("L'année de publication doit être supérieure ou égale à 1990.")
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication


    @abstractmethod
    def afficher_details(self):
        pass

    def modifier_details(self, titre=None ,auteur=None, annee_publication=None):
        if titre:
            self.titre = titre
        if auteur:
            self.auteur = auteur
        if annee_publication:
            if annee_publication < 1990:
                raise ValueError("L'année de publication doit être supérieure ou égale à 1990.")
            self.annee_publication = annee_publication

    def __str__(self):
        return f"ID: {self.id}, Titre: {self.titre}, Auteur: {self.auteur}, Année: {self.annee_publication}"
    
class Livre(Document):
    def __init__(self, id, titre, auteur, annee_publication, isbn, nombre_pages):
        super().__init__(id, titre, auteur, annee_publication)
        self.isbn = isbn
        self.nombre_pages = nombre_pages
        
    def afficher_details(self):
        print(f"Livre - {self}: ISBN: {self.isbn}, Pages: {self.nombre_pages}")

    def __str__(self):
        return super().__str__() + f", ISBN: {self.isbn}, Pages: {self.nombre_pages}"
    
class Revue(Document):
    def __init__(self, id, titre, auteur, annee_publication, numero, frequence):
        super().__init__(id, titre, auteur, annee_publication)
        self.numero = numero
        self.frequence = frequence

    def afficher_details(self):
        print(f"Revue - {self}: Numéro: {self.numero}, Fréquence: {self.frequence}")

    def __str__(self):
        return super().__str__() + f", Numéro: {self.numero}, Fréquence: {self.frequence}"
    
class CD(Document):
    def __init__(self, id, titre, auteur, annee_publication, genre_musical, duree):
        super().__init__(id, titre, auteur, annee_publication)
        self.genre_musical = genre_musical
        self.duree = duree

    def afficher_details(self):
        print(f"CD - {self}: Genre: {self.genre_musical}, Durée: {self.duree} minutes")

    def __str__(self):
        return super().__str__() + f", Genre: {self.genre_musical}, Durée: {self.duree} minutes"
    
class Bibliotheque:
    def __init__(self):
        self.documents = []

    def ajouter_document(self, document):
        self.documents.append(document)

    def supprimer_document(self, id):
        self.documents = [doc for doc in self.documents if doc.id != id]

    def mettre_a_jour_document(self, id, titre=None, auteur=None, annee_publication=None):
        for doc in self.documents:
            if doc.id == id:
                doc.modifier_details(titre, auteur, annee_publication)
            break

    def afficher_document(self):
        for doc in self.documents:
            print(doc)

    def filtrer_documents(self, critere, valeur):
        filtered = []
        for doc in self.documents:
            if critere == "auteur" and doc.auteur == valeur:
                filtered.append(doc)
            elif critere == "annee" and doc.annee_publication == valeur:
                filtered.append(doc)
        return filtered

    def sauvegarder_json(self, chemin):
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump([doc.__dict__ for doc in self.documents], f, ensure_ascii=False, indent=4)

    def sauvegarder_csv(self, chemin):
        if self.documents:
            with open(chemin, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                header = self.documents[0].__dict__.keys()
                writer.writerow(header)
                for doc in self.documents:
                    writer.writerow(doc.__dict__.values())


livre = Livre(1, "A Song of ice and fire", "George R R Martin", 1998, "123456789", 1000)
revue = Revue(2, "Majid", "Majin inc", 2022, 10, "Mensuel")
cd = CD(3, "Brave", "Walt Disney", 2021, "Action", 70)


biblio = Bibliotheque()
biblio.ajouter_document(livre)
biblio.ajouter_document(revue)
biblio.ajouter_document(cd)

biblio.afficher_document()

biblio.sauvegarder_json("bibliotheque.json")
biblio.sauvegarder_csv("bibliotheque.csv")