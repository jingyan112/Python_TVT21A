#osa10-11
"""
Implement Henkilo class with name, number, address attributes and corresponding methods.
Modify Puhelinluettelo class by storing the person information (name, number, address) through Henkilo class.
Expand the solution with a command 3 that allows you to add address for a person. (add_address method in PuhelinluetteloSovellus)
Modify the haku method in PuhelinluetteloSovellus and add method lisaa_osoite to display the number and address info when searching by name.
"""
# class person: name, number, address
class Henkilo:
    def __init__(self, nimi: str):
        self._nimi = nimi
        self._numerot = []
        self._osoite = None
    
    def nimi(self):
        return self._nimi
    
    def numerot(self):
        return self._numerot
    
    def osoite(self):
        return self._osoite

    def lisaa_numero(self, numero: str):
        self._numerot.append(numero)
    
    def lisaa_osoite(self, osoite: str):
        self._osoite = osoite

class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_numero(numero)

    def lisaa_osoite(self, nimi: str, osoite: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_osoite(osoite)

    def hae_tiedot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi]

    def kaikki_tiedot(self):
        return self.__henkilot

class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 numeron lisäys")
        print("2 haku")
        print("3 osoitteen lisäys")

    def numeron_lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    def add_address(self):
        nimi = input("nimi: ")
        address = input("osoite: ")
        self.__luettelo.lisaa_osoite(nimi, address)

    def haku(self):
        nimi = input("nimi: ")
        if self.__luettelo.hae_tiedot(nimi) == None:
            print("osoite ei tiedossa")
            print("numero ei tiedossa")
        else:
            numerot = self.__luettelo.hae_tiedot(nimi).numerot()
            address = self.__luettelo.hae_tiedot(nimi).osoite()
            if numerot == []:
                print("numero ei tiedossa") 
            for numero in numerot:
                print(numero)
            if address == None:
                print("osoite ei tiedossa")
            else:
                print(address)

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.numeron_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.add_address()
            else:
                self.ohje()

sovellus = PuhelinluetteloSovellus()
sovellus.suorita()

"""
Examples:
yanjing@yanjingdeMacBook-Pro src % cd /Users/yanjing/Downloads/osa10/*/src; python3 *.py
komennot:
0 lopetus
1 numeron lisäys
2 haku
3 osoitteen lisäys

komento: 1
nimi: Erkki
numero: 02-123456

komento: 3
nimi: Emilia
osoite: Viherlaaksontie 7, Espoo

komento: 2
nimi: Erkki
02-123456
osoite ei tiedossa

komento: 2
nimi: Emilia
numero ei tiedossa
Viherlaaksontie 7, Espoo

komento: 3
nimi: Erkki
osoite: Linnankatu 75, Turku

komento: 2
nimi: Erkki
02-123456
Linnankatu 75, Turku

komento: 2
nimi: Wilhelm
osoite ei tiedossa
numero ei tiedossa

komento: 0
"""