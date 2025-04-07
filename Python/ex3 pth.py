ch = input("Donner une chaîne de caractères : ")
resultat = ""

for char in ch:
    resultat = resultat + char 
    if char == 'o': 
        break 
if 'o' in ch:
    print(resultat) 