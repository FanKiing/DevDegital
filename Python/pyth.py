films = []

def add_film(films):
    while True:
        try:
            titre = input("Entrer le titre: ")
            genre = input("Entrer le genre: ")
            annee_de_sortie = int(input("Entrer l'année de sortie: "))
            recettes_mondiales = float(input("Entrer les recettes mondiales: "))
            note_moyenne = float(input("Entrer la note moyenne: "))
            break
        except ValueError as e:
            print(f"Erreur: {e}")
    doc = {'Titre': titre, 'Genre': genre, 'Année de sortie': annee_de_sortie, 'Recettes mondiales': recettes_mondiales, 'Note moyenne': note_moyenne}
    films.append(doc)

def calculer_recettes_moyennes(films):
    if len(films) == 0:
        return 0
    recettes_moyennes = sum(film['Recettes mondiales'] for film in films) / len(films)
    return recettes_moyennes

def get_genres(films):
    return set(film['Genre'] for film in films)
    

def enrichir_donnees_films(films):
    for film in films:
        recettes_mondiales = film['Recettes mondiales']
        if recettes_mondiales < 100:
            categorie_recettes = "Faible"
        elif 100 <= recettes_mondiales < 500:
            categorie_recettes = "Modérée"
        else:
            categorie_recettes = "Élevée"
        film['Catégorie de recettes'] = categorie_recettes
    return films







while True:
    print("1. Ajouter un film")
    print("2. Calculer les recettes moyennes")
    print("3. Afficher les genres")
    print("4. Quitter")

    choice = input("Entrer votre choix: ")

    if choice == "1":
        add_film(films)
    elif choice == "2":
        print(calculer_recettes_moyennes(films))
    elif choice == "3":
        print(get_genres(films))
    elif choice == "4":
        print("Au revoir!")
        break