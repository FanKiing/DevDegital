class IPv4:
    def __init__(self, segments):
        if len(segments) != 4:
            raise ValueError("Une adresse IPv4 doit avoir exactement 4 segments")
        if not all (0<= segment <= 255 for segment in segments):
            raise ValueError("Chaque segments doit être compris entre 0 et 255.")
        self.segments = segments

    def adresse_reseau(self,masque):
        if len(masque) !=4 or not all (0<= m <= 255 for m in masque):
            raise ValueError("Le masque doit avoir 4 segments entre 0 et 255")
        return [self.segments[i] & masque[i] for i in range(4)]
    
    def masque(self):
        classe = self.classe()
        if classe == "A":
            return [255, 0, 0, 0]
        elif classe == "B":
            return [255, 255 ,0 ,0]
        elif classe == "C":
            return [255, 255, 255, 0]
        else:
            raise ValueError("Masque indéfini pour cette classe d'adresse.")
        
    def classe(self):
        premier_segments = self.segments[0]
        if 0<= premier_segments <= 127 :
            return "A"
        elif 128<= premier_segments <= 191 :
            return "B"
        elif 192<= premier_segments <= 223 :
            return "C"
        elif 224<= premier_segments <= 239 :
            return "D"
        elif 240<= premier_segments <= 255 :
            return "E"
        else:
            raise ValueError("Classe indéfinie.")
        
    def GetClasse(self):
        return self.classe()
    
    def GetAdresseReseau(self):
        classe = self.classe()
        if classe == "A" :
            return [self.segments[0], 0 , 0, 0]
        elif classe == "B" :
            return [self.segments[0], self.segments[1], 0 ,0]
        elif classe == "C" :
            return [self.segments[0], self.segments[1], self.segments[2], 0]
        else:
            raise ValueError("Adresse réseau non définie pour cette classe.")
        
    def GetMasque(self):
        return self.masque()
    

ip = IPv4([192, 168, 1, 10])
print("Classe:", ip.GetClasse())
print("Masque:", ip.GetMasque())
print("Adresse réseau:", ip.GetAdresseReseau())