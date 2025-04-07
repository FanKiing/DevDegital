
class Voiture:
    nbr_voiture=0
    def __init__(self,m,mo,a,kilo=0):
        self.marque=m 
        self.modele=mo
        self.annee=a  
        self.kilometrage=kilo  
        Voiture.nbr_voiture+=1
    def demarrer(self):
        print("la voiture demarre !!!")
    def rouler(self,newKilo):
        self.kilometrage=newKilo
    def __str__(self):
        return f"{self.marque} ** {self.modele} ** {self.annee} ** {self.kilometrage}"
        
        
v=Voiture("m1","mo1",2000,120)
print(v)
v2=Voiture("m1","mo1",2000,120)
print(Voiture.nbr_voiture)
v.rouler(500)
print(v)