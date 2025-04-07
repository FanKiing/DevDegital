from abc import ABC, abstractmethod 
import math 
 
class Calculatrice(ABC): 
    def __init__(self): 
        self.operande = "" 
        self.resultat = 0 
     
    @abstractmethod 
    def calculer(self): 
        pass 
 
    def afficher_resultat(self): 
        return self.resultat 
 
class CalculatriceScientifique(Calculatrice): 
    def __init__(self): 
        super().__init__() 
     
    def calculer(self, expression): 
        try: 
            self.operande = expression 
            # Ici on peut ajouter un calcul simple ou scientifique 
            if "sin" in expression: 
                self.resultat = math.sin(math.radians(float(expression[3:]))) 
            elif "cos" in expression: 
                self.resultat = math.cos(math.radians(float(expression[3:]))) 
            elif "tan" in expression: 
                self.resultat = math.tan(math.radians(float(expression[3:]))) 
            else: 
                self.resultat = eval(expression)  # Utilisation de eval pour les autres calculs 
        except Exception as e: 
            self.resultat = "Erreur"
