class Livre:
    def __init__(self, titre, auteur, nombre_pages, statut="disponible"):
        self.titre = titre
        self.auteur = auteur
        self.nombre_pages = nombre_pages
        self.statut = statut

    def emprunter(self):
        self.statut = "emprunté"

    def retourner(self):
        self.statut = "disponible"

    def __str__(self):
        return f"Livre : {self.titre} de {self.auteur}, {self.nombre_pages} pages, statut : {self.statut}"

    def __repr__(self):
        return f"Livre(titre='{self.titre}', auteur='{self.auteur}', nombre_pages={self.nombre_pages}, statut='{self.statut}')"

class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        self.livres_empruntes.append(livre)
        livre.emprunter()

    def retourner_livre(self, livre):
        self.livres_empruntes.remove(livre)
        livre.retourner()

    def __str__(self):
        return f"Utilisateur : {self.nom}, livres empruntés : {[livre.titre for livre in self.livres_empruntes]}"

    def __repr__(self):
        return f"Utilisateur(nom='{self.nom}', livres_empruntes={self.livres_empruntes})"

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres_disponibles(self):
        return [livre for livre in self.livres if livre.statut == "disponible"]

    @staticmethod
    def afficher_total_livres_empruntes():
        total = 0
        for bibliotheque in Bibliotheque.instances:
            total += len(bibliotheque.afficher_livres_empruntes())
        return total

    def __str__(self):
        return f"Bibliotheque avec {len(self.livres)} livres"

    def __repr__(self):
        return f"Bibliotheque(livres={self.livres})"

class LivreEmprunte(Livre):
    def __init__(self, titre, auteur, nombre_pages, date_emprunt):
        super().__init__(titre, auteur, nombre_pages, "emprunté")
        self.date_emprunt = date_emprunt

    def __str__(self):
        return f"Livre emprunté : {self.titre} de {self.auteur}, {self.nombre_pages} pages, emprunté le {self.date_emprunt}"

    def __repr__(self):
        return f"LivreEmprunte(titre='{self.titre}', auteur='{self.auteur}', nombre_pages={self.nombre_pages}, date_emprunt='{self.date_emprunt}')"

bibliotheque = Bibliotheque()

livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 93)
livre2 = Livre("Les Misérables", "Victor Hugo", 1234)
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)

print("Livres disponibles :")
for livre in bibliotheque.afficher_livres_disponibles():
    print(livre)

utilisateur = Utilisateur("Jean")

utilisateur.emprunter_livre(livre1)

print("Livres empruntés :")
for livre in bibliotheque.afficher_livres_empruntes():
    print(livre)

utilisateur.retourner_livre(livre1)

print("Livres disponibles :")
for livre in bibliotheque.afficher_livres_disponibles():
    print(livre)

livre_emprunte = LivreEmprunte("Le Comte de Monte-Cristo", "Alexandre Dumas", 1234, "2022-01-01")

print(livre_emprunte)


    