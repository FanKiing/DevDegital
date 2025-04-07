while True:
    try:
        year = int(input())
        if year < 1582:
            print("out of range")
        elif year % 4 != 0:
            print("commune")
        elif year % 100 != 0:
            print("bissextile")
        elif year % 400 != 0:
            print("commune")
        else:
            print("bissextile")
    except:
        print("voux devez saisir une valeur")
        continue
