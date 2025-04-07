class CryptoMonnaie:
    def __init__(self, name, symbol, price, market_cap, volume):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.market_cap = market_cap
        self.volume = volume

class GestionCryptoMonnaies:
    def __init__(self):
        self.crypto_monnaies = []

    def ajouter_crypto_monnaie(self, name, symbol, price, market_cap, volume):
        crypto_monnaie = CryptoMonnaie(name, symbol, price, market_cap, volume)
        self.crypto_monnaies.append(crypto_monnaie)

    def modifier_crypto_monnaie(self, symbol, name=None, price=None, market_cap=None, volume=None):
        for crypto_monnaie in self.crypto_monnaies:
            if crypto_monnaie.symbol == symbol:
                if name:
                    crypto_monnaie.name = name
                if price:
                    crypto_monnaie.price = price
                if market_cap:
                    crypto_monnaie.market_cap = market_cap
                if volume:
                    crypto_monnaie.volume = volume
                return
        print("Crypto-monnaie non trouvée")

    def supprimer_crypto_monnaie(self, symbol):
        for crypto_monnaie in self.crypto_monnaies:
            if crypto_monnaie.symbol == symbol:
                self.crypto_monnaies.remove(crypto_monnaie)
                return
        print("Crypto-monnaie non trouvée")

    def rechercher_crypto_monnaie(self, name=None, symbol=None):
        for crypto_monnaie in self.crypto_monnaies:
            if (name and crypto_monnaie.name == name) or (symbol and crypto_monnaie.symbol == symbol):
                return crypto_monnaie
        return None

    def filtrer_crypto_monnaies(self, prix=None, market_cap=None, operator=">"):
        result = []
        for crypto_monnaie in self.crypto_monnaies:
            if prix and eval(f"crypto_monnaie.price {operator} prix"):
                result.append(crypto_monnaie)
            elif market_cap and eval(f"crypto_monnaie.market_cap {operator} market_cap"):
                result.append(crypto_monnaie)
        return result

    def trier_crypto_monnaies(self, champ="price", order="asc"):
        if order == "asc":
            return sorted(self.crypto_monnaies, key=lambda x: getattr(x, champ))
        else:
            return sorted(self.crypto_monnaies, key=lambda x: getattr(x, champ), reverse=True)

    def top_n_crypto_monnaies(self, n):
        return self.trier_crypto_monnaies("market_cap", "desc")[:n]

    def moyenne_prix(self):
        return sum(crypto_monnaie.price for crypto_monnaie in self.crypto_monnaies) / len(self.crypto_monnaies)

    def moyenne_market_cap(self):
        return sum(crypto_monnaie.market_cap for crypto_monnaie in self.crypto_monnaies) / len(self.crypto_monnaies)

    def crypto_monnaie_max_market_cap(self):
        return max(self.crypto_monnaies, key=lambda x: x.market_cap)

    def crypto_monnaie_max_volume(self):
        return max(self.crypto_monnaies, key=lambda x: x.volume)


    

    
    