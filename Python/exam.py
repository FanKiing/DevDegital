#Ex1

kilometres = int(input("Veuillez saisir le nombre de kilomètres parcourus : "))
cout_par_km = int(input("Veuillez saisir le coût par kilomètre : "))

cout_total = kilometres * cout_par_km

if kilometres > 100:
    cout_total *= 0.90

print("Le coût total du voyage est :", cout_total)

#Ex2

nombre = int(input("Veuillez saisir un nombre entier : "))

if nombre % 2 == 0:
    print("Le nombre est pair")
else:
    print("Le nombre est impair")


