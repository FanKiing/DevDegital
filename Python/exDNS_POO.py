import re

class DomaineExistantException(Exception):
    pass

class DomaineInexistantException(Exception):
    pass

class FormatInvalideException(Exception):
    pass

class DNS:
    def __init__(self):
        self.enregistrements = {}
        self.journal = []

    @staticmethod
    def valider_domaine(domaine):
        pattern = r"^(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
        if not re.match(pattern, domaine):
            raise FormatInvalideException(f"Domaine invalide : {domaine}")

    @staticmethod
    def valider_ip(ip):
        pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
        if not re.match(pattern, ip) or any(int(octet) > 255 for octet in ip.split(".")):
            raise FormatInvalideException(f"Adresse IP invalide : {ip}")

    def ajouter_enregistrement(self, domaine, ip):
        self.valider_domaine(domaine)
        self.valider_ip(ip)
        if domaine in self.enregistrements:
            raise DomaineExistantException(f"Le domaine {domaine} existe déjà.")
        self.enregistrements[domaine] = ip
        self.journal.append(f"Ajout : {domaine} -> {ip}")

    def rechercher_ip(self, domaine):
        self.valider_domaine(domaine)
        if domaine not in self.enregistrements:
            raise DomaineInexistantException(f"Le domaine {domaine} n'existe pas.")
        return self.enregistrements[domaine]

    def mettre_a_jour_enregistrement(self, domaine, nouvelle_ip):
        self.valider_domaine(domaine)
        self.valider_ip(nouvelle_ip)
        if domaine not in self.enregistrements:
            raise DomaineInexistantException(f"Le domaine {domaine} n'existe pas.")
        ancienne_ip = self.enregistrements[domaine]
        self.enregistrements[domaine] = nouvelle_ip
        self.journal.append(f"Mise à jour : {domaine} -> {nouvelle_ip} (ancien : {ancienne_ip})")

    def supprimer_enregistrement(self, domaine):
        self.valider_domaine(domaine)
        if domaine not in self.enregistrements:
            raise DomaineInexistantException(f"Le domaine {domaine} n'existe pas.")
        del self.enregistrements[domaine]
        self.journal.append(f"Suppression : {domaine}")

    def afficher_journal(self):
        return "\n".join(self.journal)
    

dns = DNS()

try:
    dns.ajouter_enregistrement("example.com", "192.168.1.1")
    print("Domaine ajouté avec succès.")
except FormatInvalideException as e:
    print(e)
except DomaineExistantException as e:
    print(e)

try:
    dns.ajouter_enregistrement("example.com", "192.168.1.2")
except FormatInvalideException as e:
    print(e)
except DomaineExistantException as e:
    print(e)

try:
    ip = dns.rechercher_ip("example.com")
    print(f"L'adresse IP pour example.com est {ip}")
except FormatInvalideException as e:
    print(e)
except DomaineInexistantException as e:
    print(e)

try:
    dns.mettre_a_jour_enregistrement("example.com", "192.168.1.10")
    print("Mise à jour effectuée.")
except FormatInvalideException as e:
    print(e)
except DomaineInexistantException as e:
    print(e)

try:
    dns.supprimer_enregistrement("example.com")
    print("Domaine supprimé.")
except FormatInvalideException as e:
    print(e)
except DomaineInexistantException as e:
    print(e)

print("\nJournal des actions :")
print(dns.afficher_journal())

