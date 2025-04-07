from datetime import datetime, timedelta
import re

class InvalidDateException(Exception):
    pass

class AgeConstraintException(Exception):
    pass

class Employe:
    def __init__(self, matricule, nom, prenom, dateNaissance, dateEmbauche, salaire):
        self.matricule = matricule

        if not isinstance(nom, str) or not re.fullmatch(r'[A-Z]{2,}(\s[A-Z]{2,})*', nom):
            raise ValueError("Le nom doit correspondre au pattern [A-Z]{2,}(\\s[A-Z]{2,})*")
        
        self.nom = nom

        if not isinstance(prenom, str) or not re.fullmatch(r'[A-Z][a-z]{2,}(\s[A-Z][a-z]{2,})', prenom):
            raise ValueError("Le prènom doit correspondre au pattern [A-Z][a-z]{2,}(\\s[A-Z][a-z]{2,})")
        
        self.prenom = prenom

        if not isinstance(dateNaissance, datetime):
            raise TypeError("La date de naissance doit être un objet datetime")
        

        if dateNaissance >= datetime(2001,1,1):
            raise InvalidDateException("La date de naissance doit être antérieure au 1er janvier 2000")
        
        self.dateNaissance = dateNaissance

        if not isinstance(dateEmbauche, datetime):
            raise TypeError("La date de l'embauche doit être un objet datetime")

        ageEmbauche = (dateEmbauche - dateNaissance).days //365

        if ageEmbauche < 24:
            raise AgeConstraintException("L'employé doit avoir au moins 24 ans au moment de l'embauche")
        
        self.dateEmbauche = dateEmbauche
        self.salaire = salaire

    def __str__(self):
        return f"Employé {self.matricule} - {self.nom} {self.prenom}\nDate de naissance: {self.dateNaissance.strftime('%Y-%m-%d')}\nDate d'embauche: {self.dateEmbauche.strftime('%Y-%m-%d')}\nSalaire: {self.salaire}"
    
    def __eq__(self, other):
        if not isinstance(other, Employe):
            return False
        return self.matricule == other.matricule
    
    def calcul_anciennete(self):
        return (datetime.now() - self.dateEmbauche).days // 365
    
    def calcul_age(self):
        return (datetime.now() - self.dateNaissance).days // 365
    
    def calcul_date_retraite(self):
        age_retraite = 65
        retraited_date = self.dateNaissance + timedelta(days=age_retraite  * 365)
        return retraited_date

if __name__ == "__main__":
    try:
        emp = Employe(
            matricule="12345",
            nom="ESSAIH",
            prenom="Yassir",
            dateNaissance=datetime(2003, 8, 16),
            dateEmbauche=datetime(2020, 6, 15),
            salaire=45000
            )
        print(emp)
        print("Ancienneté:", emp.calcul_anciennete(), "ans")
        print("Age:", emp.calcul_age(), "ans")
        print("Date de retraite:", emp.calcul_date_retraite().strftime('%Y-%m-%d'))

    except (InvalidDateException, AgeConstraintException, ValueError, TypeError) as e:
        print("Error:", e)