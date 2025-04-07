import sqlite3

class DbManager:
    def __init__(self, nom_base="app.db"):

        try:
            self.connexion = sqlite3.connect(nom_base)
            print(f"Connected to database: {nom_base}")
            self.creer_table()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def creer_table(self):

        try:
            requete = """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """
            self.connexion.execute(requete)
            self.connexion.commit()
            print("Table 'items' is ready.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            raise

    def creer(self, nom):
        try:
            requete = "INSERT INTO items (name) VALUES (?)"
            self.connexion.execute(requete, (nom,))
            self.connexion.commit()
            print(f"Item '{nom}' created successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting item: {e}")
            raise

    def lire_tous(self):
        try:
            requete = "SELECT * FROM items"
            curseur = self.connexion.execute(requete)
            return curseur.fetchall()
        except sqlite3.Error as e:
            print(f"Error reading all items: {e}")
            raise

    def mettre_a_jour(self, id_item, nouveau_nom):

        try:
            requete = "UPDATE items SET name = ? WHERE id = ?"
            self.connexion.execute(requete, (nouveau_nom, id_item))
            self.connexion.commit()
            print(f"Item with ID {id_item} updated to '{nouveau_nom}'.")
        except sqlite3.Error as e:
            print(f"Error updating item: {e}")
            raise

    def supprimer(self, id_item):
        try:
            requete = "DELETE FROM items WHERE id = ?"
            self.connexion.execute(requete, (id_item,))
            self.connexion.commit()
            print(f"Item with ID {id_item} deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting item: {e}")
            raise

    def __del__(self):
        try:
            self.connexion.close()
            print("Database connection closed.")
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")
            raise

