
#les attributs de class : les classe de la classe comme etant objet 
class User:
    nbrInstance=0
    def __init__(self,un,pwd):
        self.__userName=un
        self.__password=pwd
        User.nbrInstance+=1
    def __str__(self):
        return f"{self.userName} --- {self.password }"
    def getUserName(self):
        return self.__userName
    
users=[ User(f'u{i+1}','1234556') for i in range(10)]

print(users[3].getUserName())
print(User.nbrInstance)