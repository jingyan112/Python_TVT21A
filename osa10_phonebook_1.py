#osa10-10
# Phonebook category {"name1": ["number1", "number2",...], ...}
"""
Expand your solution with a command 3 that allows you to search for a name by number. 
"""
class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = []
        self.__henkilot[nimi].append(numero)

    def hae_numerot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi]
    
    def search_number(self, numero: str):
        for nimi, numero_list in self.__henkilot.items():
            if numero in numero_list:
                return nimi
        return None

    def kaikki_tiedot(self):
        return self.__henkilot

# Retrieve information from the file and save information to the file
class Tiedostonkasittelija():
    def __init__(self, tiedosto):
        self.__tiedosto = tiedosto

    # Read
    def lataa(self):
        nimet = {}
        with open(self.__tiedosto) as f:
            for rivi in f:
                osat = rivi.strip().split(';')
                nimi, *numerot = osat
                nimet[nimi] = numerot
        return nimet

    # Write
    def talleta(self, luettelo: dict):
        with open(self.__tiedosto, "w") as f:
            for nimi, numerot in luettelo.items():
                rivi = [nimi] + numerot
                f.write(";".join(rivi) + "\n")

class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()
        self.__tiedosto = Tiedostonkasittelija("luettelo.txt")

        for nimi, numerot in self.__tiedosto.lataa().items():
            for numero in numerot:
                self.__luettelo.lisaa_numero(nimi, numero)

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 lisäys")
        print("2 haku")

    # Store nimi:number information
    def lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    # Search by name
    def haku(self):
        nimi = input("nimi: ")
        numerot = self.__luettelo.hae_numerot(nimi)
        if numerot == None:
            print("numero ei tiedossa") 
            return 
        for numero in numerot:
            print(numero)

    # Search by number
    def search_by_number(self):
        numero = input("numero: ")
        nimi = self.__luettelo.search_number(numero)
        if nimi == None:
            print("tuntematon numero") 
            return 
        print(nimi)      

    # Write the information to the book and quit
    def lopetus(self):
        self.__tiedosto.talleta(self.__luettelo.kaikki_tiedot())

    # Command
    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                self.lopetus()
                break
            elif komento == "1":
                self.lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.search_by_number()
            else:
                self.ohje()

sovellus = PuhelinluetteloSovellus()
sovellus.suorita()

"""

Examples:
komennot:
0 lopetus   # end
1 lisäys    # add: name and telephone number
2 haku      # search
3 haku numeron perusteella      # search by number

komento: 1
nimi: Erkki
numero: 02-123456

komento: 1
nimi: Erkki
numero: 045-4356713

komento: 3
numero: 02-123456
Erkki

komento: 3
numero: 0100100
tuntematon numero

komento: 0
"""