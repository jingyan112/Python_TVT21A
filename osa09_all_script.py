#osa9-01 Tee ratkaisusi luokan Auto perään
# Älä muuta luokkaa!
"""
Write a function nopein_auto(autot: list) that gets Autoobjects in the list class as its parameter.
The function returns the fastest car mark of the cars in the list.
You can assume that the fastest car is unambiguous. Do not change the original list or category Auto.
"""
class Auto:
    def __init__(self, merkki: str, huippunopeus: int):
        self.merkki = merkki
        self.huippunopeus = huippunopeus

    def __str__(self):
        return f"Auto (merkki: {self.merkki}, huippunopeus: {self.huippunopeus})"

def nopein_auto(autot: list):
    new_dic = {}
    for item in autot:
        new_dic[item.merkki] = item.huippunopeus
    return max(new_dic, key = new_dic.get)

# TEE RATKAISUSI TÄHÄN:
if __name__ == "__main__":
    auto1 = Auto("Mersu", 195)
    auto2 = Auto("Lada", 110)
    auto3 = Auto("Ferrari", 280)
    auto4 = Auto("Trabant", 85)

    autot = [auto1, auto2, auto3, auto4]
    print(nopein_auto(autot))

#osa9-02 Tee ratkaisusi luokan Koesuoritus perään.
# ÄLÄ MUUTA LUOKKAA
"""
Class Koesuoritus that models the test performance according to its name with two attributes, namely suorittaja(str) and pisteet(int).
Write a function hyvaksytyt(suoritukset: list, pisteraja: int) that gets as a parameter a list of test runs and the lowest accepted score as an integer.
The function creates and returns a new list in which only the approved performances from the list are stored.
Do not change the original list or category Koesuoritus.
"""
class Koesuoritus:
    def __init__(self, suorittaja: str, pisteet: int):
        self.suorittaja = suorittaja
        self.pisteet = pisteet

    def __str__(self):
        return f'Koesuoritus (suorittaja: {self.suorittaja}, pisteet: {self.pisteet})'

def hyvaksytyt(suoritukset: list, pisteraja: int):
    result = []
    for item in suoritukset:
        if item.pisteet >= pisteraja:
            result.append(item)
    return result

# TEE RATKAISUSI TÄHÄN:
if __name__ == "__main__":
    s1 = Koesuoritus("Pekka", 12)
    s2 = Koesuoritus("Pirjo", 19)
    s3 = Koesuoritus("Pauli", 15)
    s4 = Koesuoritus("Pirkko", 9)
    s5 = Koesuoritus("Petriina", 17)

    hyv = hyvaksytyt([s1, s2, s3, s4, s5], 15)
    for hyvaksytty in hyv:
        print(hyvaksytty)

#osa9-03 TEE RATKAISUSI TÄHÄN:
# Huom! Älä muuta luokkaa Henkilo!
"""
- Implement punnitsethe(henkilo: Henkilo) method that is intended to return the weight of the person from Henkilo.paino.
- Implement syota(henkilo: Henkilo) method that increases the weight of the person in the parameter by one
- Implement punnitukset() method that calculates how many times the punnitse method is called
"""
class Henkilo:
    def __init__(self, nimi: str, ika: int, pituus: int, paino: int):
        self.nimi = nimi
        self.ika = ika
        self.pituus = pituus
        self.paino = paino

class Kasvatuslaitos:
    def __init__(self):
        self.punnitusten_lkm = 0

    def punnitse(self, henkilo: Henkilo):
        self.punnitusten_lkm = self.punnitusten_lkm + 1
        # palautetaan parametrina annetun henkilön paino
        return henkilo.paino
    
    def syota(self, henkilo: Henkilo):
        henkilo.paino = henkilo.paino + 1
        return henkilo.paino
    
    def punnitukset(self):
        return self.punnitusten_lkm

if __name__ == "__main__":
    haagan_neuvola = Kasvatuslaitos()

    eero = Henkilo("Eero", 1, 110, 7)
    pekka = Henkilo("Pekka", 33, 176, 85)

    print(f"{eero.nimi} painaa {haagan_neuvola.punnitse(eero)} kg")
    print(f"{pekka.nimi} painaa {haagan_neuvola.punnitse(pekka)} kg")
    print() 

    haagan_neuvola.syota(eero)
    haagan_neuvola.syota(eero)
    haagan_neuvola.syota(eero)
    print(f"{eero.nimi} painaa {haagan_neuvola.punnitse(eero)} kg")
    print(f"{pekka.nimi} painaa {haagan_neuvola.punnitse(pekka)} kg")

    print(f"Punnituksia tehty {haagan_neuvola.punnitukset()}")

    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)
    print(f"Punnituksia tehty {haagan_neuvola.punnitukset()}")

    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)
    print(f"Punnituksia tehty {haagan_neuvola.punnitukset()}")