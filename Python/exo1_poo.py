
class Voiture:
    def __init__(self,m,mo,a,kilo=0):
        self.marque=m 
        self.modele=mo
        self.annee=a  
        self.kilometrage=kilo  
    def demarrer(self):
        print("la voiture demarre !!!")
    def rouler(self,newKilo):
        self.kilometrage=newKilo
    def __str__(self):
        return f"{self.marque} ** {self.modele} ** {self.annee} ** {self.kilometrage}"
        
        
v=Voiture("m1","mo1",2000,120)
print(v)

v.rouler(500)
print(v)