from datetime import datetime, timedelta
from random import random

def enter_date():
    input_date = input("Enter un date (YYYY-MM-DD): ")
    age = datetime.now() - datetime.strptime(input_date, "%Y-%m-%d")
    print("Vous avez", age.days // 365, "ans")

def difference():
    date1 = input("Date 1 (YYYY-MM-DD): ")
    date2 = input("Date 2 (YYYY-MM-DD): ")
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")
    difference = date2 - date1
    print("La difference entre les deux dates est de", difference.days, "jours")

def add_days():
    date = input("Date (YYYY-MM-DD): ")
    days = int(input("Nombre de jours à ajouter: "))
    date = datetime.strptime(date, "%Y-%m-%d")
    new_date = date + datetime.timedelta(days=days)
    print("La nouvelle date est", new_date.strftime("%Y-%m-%d"))

def day_specifier():
    input_date = input("Enter un date (YYYY-MM-DD): ")
    age = datetime.strptime(input_date, "%Y-%m-%d")
    week = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    print("Le jour de la semaine correspondant est", week[age.weekday()])

def year_end():
    input_date = input("Enter un date (YYYY-MM-DD): ")
    converted = datetime.strptime(input_date, "%Y-%m-%d")
    year_end = datetime(converted.year, 12, 31)
    counter = year_end - converted
    print("Il reste", counter.days, "jours avant la fin de l'annee")

def convert_date():
    input_date = input("Enter un date (YYYY-MM-DD): ")
    r = input_date.replace("-", "/")
    print(r)
    r = r[6:10] + "/" + r[3:5] + "/" + r[0:2]
    print("La nouvelle date est", r)

def valid_date():
    input_date = input("Enter un date (YYYY-MM-DD): ")
    try:
        datetime.strptime(input_date, "%Y-%m-%d")
        print("La date est valide")
    except ValueError:
        print("La date est invalide")

def jours_ouvrés():
    input_date = input("Enter un date (YYYY-MM-DD): ")
    try:
        datetime.strptime(input_date, "%Y-%m-%d")
    except ValueError:
        print("La date est invalide")
    date_debut = datetime.datetime.strptime(date_debut, "%Y-%m-%d")
    date_fin = datetime.datetime.strptime(date_fin, "%Y-%m-%d")

    jours_ouvrés = 0

    while date_debut <= date_fin:
        if date_debut.weekday() < 5:
            jours_ouvrés += 1
        date_debut += datetime.timedelta(days=1)

    return jours_ouvrés

def afficher_dates_du_mois():
    mois = int(input("Entrez le mois (1-12): "))
    annee = int(input("Entrez l'année: "))
    date_debut = datetime.datetime(annee, mois, 1)
    date_fin = datetime.datetime(annee, mois, 31)

    while date_debut <= date_fin:
        print(date_debut.strftime("%Y-%m-%d"))
        date_debut += datetime.timedelta(days=1)
    print("Nombre de jours ouvrés:", jours_ouvrés(date_debut, date_fin))

def calculer_duree(heure_debut, heure_fin):
    input_date = input("Enter un date (YYYY-MM-DD): ")
    debut_minutes = int(heure_debut[:2]) * 60 + int(heure_debut[3:])
    fin_minutes = int(heure_fin[:2]) * 60 + int(heure_fin[3:])

    duree_minutes = fin_minutes - debut_minutes

    heures = duree_minutes // 60
    minutes = duree_minutes % 60

    return f"{heures} heures et {minutes} minutes"

def generate_random_dates(start_date, end_date, count=10):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    delta = end_date - start_date
    dates = [start_date + timedelta(days=random.randint(0, delta.days)) for _ in range(count)]
    return [date.strftime("%Y-%m-%d") for date in dates]

def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

def replace_word(sentence, old_word, new_word):
    words = sentence.split()
    new_sentence = " ".join([new_word if word == old_word else word for word in words])
    return new_sentence

def reverse_word(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

def is_palindrome(sentence):
    return sentence == sentence[::-1]

def holiday_reminder():
    date = input("Enter a date (YYYY-MM-DD): ")
    date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.today()
    delta = date - today
    days_until_holiday = delta.days
    if days_until_holiday <= 0:
        print("Today is", date.strftime("%Y-%m-%d"))
    else:
        print("You have", days_until_holiday, "days until", date.strftime("%Y-%m-%d"))

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in sentence if char in vowels)
    return count

def count_consonants(sentence):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = sum(1 for char in sentence if char in consonants)
    return count


#Ex1

def analyze_text(text):
    mots = text.split()
    nb_mots = len(mots)

    lettres = [char for char in text if char.isalpha()]
    nb_lettres = len(lettres)

    phrases = text.split(".")
    nb_phrases = len(phrases)

    caracteres_speciaux = [char for char in text if not char.isalnum() and not char.isspace()]
    nb_caracteres_speciaux = len(caracteres_speciaux)

    mots_majuscules = [mot for mot in mots if mot[0].isupper()]
    nb_mots_majuscules = len(mots_majuscules)

    mots_points = [mot for mot in mots if mot[-1] == "."]
    nb_mots_points = len(mots_points)

    print("Nombre de mots :", nb_mots)
    print("Nombre de lettres :", nb_lettres)
    print("Nombre de phrases :", nb_phrases)
    print("Nombre de caractères spéciaux :", nb_caracteres_speciaux)
    print("Nombre de mots commençant par une majuscule :", nb_mots_majuscules)
    print("Nombre de mots se terminant par un point :", nb_mots_points)



#P1
#Ex2

from datetime import datetime

def date_difference(date1, date2):
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")

    difference = date2 - date1

    jours = difference.days
    heures = difference.seconds // 3600
    minutes = (difference.seconds // 60) % 60
    secondes = difference.seconds % 60

    print(f"La différence entre les deux dates est de {jours} jours, {heures} heures, {minutes} minutes et {secondes} secondes.")

#Ex3

def afficher_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(j + 1, end=" ")
        print()


#P2

import csv

employes = [
    {"nom": "Yasser", "date_recrutement": "2020-01-01", "salaire": 40000, "departement": "Informatique"},
    {"nom": "Mohamed", "date_recrutement": "2019-06-01", "salaire": 50000, "departement": "Marketing"},
    {"nom": "Lmaati", "date_recrutement": "2018-03-01", "salaire": 60000, "departement": "Informatique"},
    {"nom": "Omar", "date_recrutement": "2020-09-01", "salaire": 70000, "departement": "RH"},
    {"nom": "Luc", "date_recrutement": "2017-12-01", "salaire": 80000, "departement": "Finance"}
]

def salaire_moyen(employes):
    salaires = [employe["salaire"] for employe in employes]
    return sum(salaires) / len(salaires)

def nombre_employes_par_departement(employes):
    departements = {}
    for employe in employes:
        departement = employe["departement"]
        if departement not in departements:
            departements[departement] = 0
        departements[departement] += 1
    return departements

def enrichissement_des_donnees(employes):
    for employe in employes:
        salaire_annuel = employe["salaire"] * 12
        employe["salaire_annuel"] = salaire_annuel
        if salaire_annuel < 50000:
            employe["classification"] = "Débutant"
        elif salaire_annuel < 80000:
            employe["classification"] = "Confirmé"
        else:
            employe["classification"] = "Expérimenté"
    return employes

def suppression_des_employes(employes, critere):
    employes_supprimes = []
    for employe in employes:
        if critere(employe):
            employes_supprimes.append(employe)
    return [employe for employe in employes if employe not in employes_supprimes]

def sauvegarde_des_donnees(employes, fichier_csv):
    with open(fichier_csv, "w", newline="") as csvfile:
        fieldnames = ["nom", "date_recrutement", "salaire", "departement", "salaire_annuel", "classification"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for employe in employes:
            writer.writerow(employe)







    