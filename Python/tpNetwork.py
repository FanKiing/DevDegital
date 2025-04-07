import re
from abc import ABC, abstractmethod
import ipaddress

class NetworkComponent(ABC):

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def fonctionner(self):
        pass

class IPv4(NetworkComponent):
    def __init__(self, adresse):
        self.adresse = adresse
        self.ip_list = self.adresse.split('.')
        self.clss = self.getClass()
        self.masque = self.getMasque()

    def info(self):
        return f"Adresse IPv4: {self.adresse}"

    def fonctionner(self):
        return "Gestion des adresses IPv4."

    def isValidIPV4(self):
        pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        if re.match(pattern, self.adresse):
            octets = self.adresse.split('.')
            return all(0 <= int(octet) <= 255 for octet in octets)
        return False

    def getClass(self):
        if not self.isValidIPV4():
            return "Adresse IPv4 invalide."
        first_octet = int(self.ip_list[0])
        if first_octet <= 127:
            return "A"
        elif first_octet <= 191:
            return "B"
        elif first_octet <= 223:
            return "C"
        elif first_octet <= 239:
            return "D"
        else:
            return "E"

    def getMasque(self):
        if self.clss == "A":
            return "255.0.0.0"
        elif self.clss == "B":
            return "255.255.0.0"
        elif self.clss == "C":
            return "255.255.255.0"
        elif self.clss == "D" or self.clss == "E":
            return "Non applicable"
        else:
            return "Adresse IPv4 invalide."

    def getIdReseau(self):
        if not self.isValidIPV4():
            return "Adresse IPv4 invalide."
        if self.clss == "A":
            return f"{self.ip_list[0]}.0.0.0"
        elif self.clss == "B":
            return f"{self.ip_list[0]}.{self.ip_list[1]}.0.0"
        elif self.clss == "C":
            return f"{self.ip_list[0]}.{self.ip_list[1]}.{self.ip_list[2]}.0"
        else:
            return "Non applicable"

    def IdHost(self):
        if not self.isValidIPV4():
            return "Adresse IPv4 invalide."
        network_id = self.getIdReseau()
        if network_id == "Non applicable":
            return "Non applicable"
        return '.'.join(str(int(o1) - int(o2)) for o1, o2 in zip(self.adresse.split('.'), network_id.split('.')))

    def getNbrOfHosts(self):
        masque = self.getMasque()
        if masque == "Non applicable":
            return 0
        try:
            network = ipaddress.IPv4Network(f"{self.adresse}/{masque}", strict=False)
            return network.num_addresses - 2
        except ValueError:
            return "Erreur dans le calcul des hôtes."

class DNS(NetworkComponent):
    def __init__(self):
        self.registre = {}
        self.cache = {}

    def info(self):
        return "Service DNS : Résolution des noms de domaine."
    
    def fonctionner(self):
        return "Gestion des noms de domaine."

    def ajouterAuRegistre(self, domain, ip):
        self.registre[domain] = ip

    def supprimerDuRegistre(self, domain):
        if domain in self.registre:
            del self.registre[domain]

    def resoudre(self, domain):
        if domain in self.cache:
            return self.cache[domain]
        if domain in self.registre:
            ip = self.registre[domain]
            self.cache[domain] = ip
            return ip
        return "Domaine non trouvé."

    def viderCache(self):
        self.cache.clear()

    def listeRegistre(self):
        return list(self.registre.keys())

    def listeCache(self):
        return list(self.cache.keys())

class DHCP(NetworkComponent):
    def __init__(self, poolAdresses):
        self.poolAdresses = poolAdresses
        self.attributions = {}

    def info(self):
        return "Service DHCP : Attribution dynamique des adresses IP."

    def fonctionner(self):
        return "Gestion dynamique des adresses IP."

    def attribuerAdresse(self, device):
        if device in self.attributions:
            return self.attributions[device]
        if not self.poolAdresses:
            return "Plus d'adresses disponibles."
        ip = self.poolAdresses.pop(0)
        self.attributions[device] = ip
        return ip

    def libererAdresse(self, device):
        if device in self.attributions:
            ip = self.attributions.pop(device)
            self.poolAdresses.append(ip)

    def listeAttributions(self):
        return self.attributions

    def listePool(self):
        return self.poolAdresses

# Example Usage
ipv4 = IPv4("192.168.1.1")
print(ipv4.info())
print(ipv4.fonctionner())
print(ipv4.isValidIPV4())
print(ipv4.getClass())
print(ipv4.getMasque())
print(ipv4.getIdReseau())
print(ipv4.IdHost())
print(ipv4.getNbrOfHosts())

dns = DNS()
dns.ajouterAuRegistre("example.com", "192.168.1.100")
print(dns.resoudre("example.com"))

dhcp = DHCP(["192.168.1.200", "192.168.1.201", "192.168.1.202"])
print(dhcp.attribuerAdresse("device1"))
print(dhcp.attribuerAdresse("device2"))
dhcp.libererAdresse("device1")
print(dhcp.listeAttributions())
print(dhcp.listePool())
