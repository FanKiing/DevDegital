# les types simples : int , float double boolean
#les dictionnaires : definir des variables contenants des entites complexes
#classe sert a creer des dictionnaires : pour créer des variables de types complexes
# une classe est plan et en se  basant sur ce plan on peut créer des objets(variables) de type complexes respectant les formalismes du plan
# la classe utilise un constructeur pour créer un objet de type complexe 
# le constructeur (__init__) définit la liste des clés des dictionnaires qui vont être crés en se basant sur la classe courante 
# la classe est en meme temps dictionnaire(list of key value pairs) et createur de dictionnaire
class User:
    def __init__(self,l,pwd):
        self.login=l
        self.password=pwd
    def __str__(self):
        return f"{self.login} ** {self.password}"
    def changeChange(self,newPwd):
        self.password=newPwd

u1=User("u1@email.com","123456")
print(u1)
u1.changeChange('abcdefg')
print(u1)


        

