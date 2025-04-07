"""
        •	Créer une classe => ajouter un nouveau type à la liste des types
        •	Classe est modèle , un plan qui décrit la structure (attributs et méthodes des objets)
        •	Objet est une variable complexe de type classe
        •	Pour construire un objet on doit appeler le constructeur de la classe
        •	Les constructeurs de la classe sont des méthodes magiques qui portent le nom __init__
        •	Une classe peut avoir plusieurs constructeurs (constructeur par défaut , constructeur d’initialisation …)
        •	Une classe peut avoir d’autres méthodes magiques qui facilitent la manipulation des objets de cette classe :
        o	__str__ : -convertir un objet de type classe  en string
        o	__repre__ : si __str__ n est pas définie 
        o	__eq__   : pour définir la logique de comparaison de deux objets de type classe ( ==)
        o	__lt__ : pour vérifier si un objet est inférieur à un autre
        o	__gt__ : 
        NB. On les appelle méthode magiques parce qu’on les appelle implicitement                                              
"""
class Produit:
    def __init__(self):
        self.codeP = 0
        self.intitule = ""
        self.prix = 0

    def __init__(self, c, nom, p):
        self.codeP = c
        self.intitule = nom
        self.prix = p

    def __str__(self):
        return f'{self.codeP}-{self.intitule}-{self.prix}'
    
    def __eq__(self, p):
        return p.codeP == self.codeP
    
    def affiche(self):
        print(f"{self.intitule}**{self.prix}")

a,b = Produit(1000, 'Ordinateur', 10000), Produit(1000, 'Ordinateur',10000)
print(a==b)
a.affiche()

class Carte:
    def __init__(self):
        self.listeP = []

    def add_product(self, product):
        product = 1
        self.listeP.append(product)

    def removeProductFrmCart(self, codeP):
        self.listeP = [product for product in self.listeP if product['codeP'] != codeP]

    def incrementQte(self,codeP):
        for product in self.listeP:
            if product['codeP'] == codeP:
                product -= 1
                if product == 0:
                    self.removeProductFrmCart(codeP)
                break

    def TotalAmount(self):
        def __str__(self):
            return sum(product['Prix'] * product for product in self.listeP)
        
    def __str__(self):
        header = f"{'CodeP':<10}{'Intitude':<15}{'Prix':<10}{'Qte':<5}\5"
        products_str = "\n".join(f"{product['codeP']:<10}{product['Intitude']:<15}{product['Prix']:<10}{product['qte']:<5}"
                                 for product in self.listeP)
        return header + products_str
    
cart = Carte()
cart.add_product({'codeP': 1000, 'Intitule': 'ordi', 'Prix' :60000})
cart.add_product({'codeP': 1001, 'Intitule': 'scanner', 'Prix':8000})
cart.incrementQte(1000)





    