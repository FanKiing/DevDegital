class PlagelPExterieureException(Exception):
    pass

class DHCPServer:
    def __init__(self, plage_ip):
        self.plage_ip = plage_ip
        self.baux = {}

    def attribuer_ip(self, client):
        if not self.plage_ip:
            raise PlagelPExterieureException("Toutes les adresses IP sont déjà attribuées.")
        ip = self.plage_ip.pop(0)
        self.baux[client] = ip
        return ip

    def liberer_ip(self, client):
        if client in self.baux:
            ip = self.baux.pop(client)
            self.plage_ip.append(ip)

    def afficher_baux(self):
        return "\n".join(f"Client: {client}, Adresse IP: {ip}" for client, ip in self.baux.items())

    def afficher_plage_ip(self):
        return ", ".join(self.plage_ip)

if __name__ == "__main__":
    plage_ip = ["192.168.1.100", "192.168.1.101", "192.168.1.102"]
    dhcp_server = DHCPServer(plage_ip)

    try:
        ip1 = dhcp_server.attribuer_ip("Client1")
        ip2 = dhcp_server.attribuer_ip("Client2")
    except PlagelPExterieureException as e:
        print(e)

    print("Baux:")
    print(dhcp_server.afficher_baux())

    dhcp_server.liberer_ip("Client1")

    print("\nAdresses IP disponibles:")
    print(dhcp_server.afficher_plage_ip())
