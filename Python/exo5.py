#methode 1
str= input('Entrez une chaine de character :')
new_str = ''
for c in str:
    if c == "0":
     new_str += "x"
    else:
        new_str += c
print(new_str)


#methode 2: en utilisant continue
str=list(input('saisir une liste de chiffre : '))
for i in range(len(str)): 
    if(str[i]=='0'):
        str[i]='x'
    continue
str=''.join(str)
print(str)