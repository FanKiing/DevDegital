class Converter:
    def __init__(self, mot):
        self.mot = mot

    def getBase(self):
        mot = self.mot
        if mot.startswith(("0b", "0B")):
            return 2
        elif mot.startswith(("0o", "0O")):
            return 8
        elif mot.startswith(("0x", "0X")):
            return 16
        else:
            try:
                int(mot)
                return 10
            except ValueError:
                raise ValueError("Le nombre n'est pas valide")

    def convert(self, to_base):
        base_origine = self.getBase()
        decimal = int(self.mot, base_origine)

        if to_base == 2:
            result = bin(decimal)[2:]
        elif to_base == 8:
            result = oct(decimal)[2:]
        elif to_base == 10:
            result = str(decimal)
        elif to_base == 16:
            result = hex(decimal)[2:]
        else:
            raise ValueError("Base de conversion non supportée")
        return result


nombre = Converter("1010")
print(nombre.convert(2))
print(nombre.convert(8))
print(nombre.convert(10))
print(nombre.convert(16))
