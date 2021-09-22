#osa8-01 tee ratkaisu tänne
"""
Make a function pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict) that takes three dictionary objects as parameters.
Each dictionary object has items that are referenced by these keys:
- "nimi": competitor 's name
- "tulos1": competitor's first result (integer between 1 ... 10)
- "tulos2": competitor's second result (integer between 1 ... 10)
- "tulos3": competitor's third result (integer between 1 ... 10)
The function calculates the averages of the results of all competitors and returns the competitor with the lowest average.
The return value of the function is a dictionary object.
"""
def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
    dic_list = [henkilo1, henkilo2, henkilo3]
    average_list = []
    for item in henkilo1, henkilo2, henkilo3:
        average_list.append((item["tulos1"] + item["tulos2"] + item["tulos3"])/3)
    return dic_list[average_list.index(min(average_list))]

if __name__ == "__main__":
    henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}
    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))

#osa8-02 tee ratkaisu tänne
"""
Make a function rivien_summat(matriisi: list) that has an integer matrix as its parameter.
The function adds a new element to each row of the matrix, the value of which is the sum of the elements in the row.
The function does not return anything, but modifies the matrix obtained as its parameter.
"""
def rivien_summat(matriisi: list):
    for item in matriisi:
        item.append(sum(item))

if __name__ == "__main__":
    matriisi = [[1, 2], [3, 4]]
    rivien_summat(matriisi)
    print(matriisi)

#osa8-03 tee ratkaisu tänne
# Muista import-lause:
"""
Make a function vuodet_listaan(paivamaarat: list) that gets a list date of objects of type of type as its parameter.
The function returns a new list with the years of the dates in order of magnitude from smallest to largest.
"""
from datetime import date

def vuodet_listaan(paivamaarat: list):
    new_list = []
    for item in paivamaarat:
        new_list.append(item.year)
    return sorted(new_list)

if __name__ == "__main__":
    paiva1 = date(2019, 2, 3)
    paiva2 = date(2006, 10, 10)
    paiva3 = date(1993, 5, 9)
    vuodet = vuodet_listaan([paiva1, paiva2, paiva3])
    print(vuodet)

#osa8-04 ÄLÄ MUUTA ALLA OLEVAA LUOKKAA Kauppalista!
# Kirjoita ratkaisusi luokan alapuolelle!
"""
Using the examples, make a function tuotteita_yhteensa(lista: Kauppalista) that gets an Kauppalistaobject of type parameter.
The function calculates the total number of products in the list and returns it.
"""
class Kauppalista:
    def __init__(self):
        self.tuotteet = []

    def tuotteita(self):
        return len(self.tuotteet)

    def lisaa(self, tuote: str, maara: int):
        self.tuotteet.append((tuote, maara))

    def tuote(self, n: int):
        return self.tuotteet[n - 1][0]

    def maara(self, n: int):
        return self.tuotteet[n - 1][1]

# ----------------------
# Tee ratkaisusi tähän:
# ----------------------
def tuotteita_yhteensa(lista: Kauppalista):
    total_num = 0
    for index in range(0, lista.tuotteita()):
        total_num = total_num + lista.maara(index)
    return total_num

if __name__ == "__main__":
    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("ananas", 1)
    print(tuotteita_yhteensa(lista))

#osa8-06 Tee ratkaisusi tähän:
"""
Make a class Kirjathat has attributes of variables nimi, kirjoittaja, genre and kirjoitusvuosi
as well as constructor that initializes the variables.
"""
from datetime import date

class Kirja:

    def __init__(self, nimi: str, kirjoittaja: str, genre: str, kirjoitusvuosi: date.year):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre
        self.kirjoitusvuosi = kirjoitusvuosi

if __name__ == "__main__":
    python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
    everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)

    print(f"{python.kirjoittaja}: {python.nimi} ({python.kirjoitusvuosi})")
    print(f"Kirjan {everest.nimi} genre on {everest.genre}")

#osa8-07 Tee ratkaisusi tähän:
"""
Create the categories requested below based on the names and types of attributes are described below each category.
For each class, also write a constructor in which the attributes are given in the order in which they are given in the description.
"""
class Muistilista:
    def __init__(self, otsikko: str, merkinnat: list):
        self.otsikko = otsikko
        self.merkinnat = merkinnat

class Asiakas:
    def __init__(self, tunniste: str, saldo: float, alennusprosentti: int):
        self.tunniste = tunniste
        self.saldo = saldo
        self.alennusprosentti = alennusprosentti

class Kaapeli:
    def __init__(self, malli: str, pituus: float, maksiminopeus: int, kaksisuuntainen: bool):
        self.malli = malli
        self.pituus = pituus
        self.maksiminopeus = maksiminopeus
        self.kaksisuuntainen = kaksisuuntainen

#osa8-7b Tee ratkaisusi tähän:
"""
Define a category Lemmikki, which has a constructor that gives values ​​to the attributes nimi, laji and syntymavuosiin that order.
Then, outside the class, write a function uusi_lemmikki(nimi: str, laji: str, syntymavuosi: int) that
creates and returns an object of Lemmikkitype new (that is, Lemmikkicorresponding to the class).
"""
class Lemmikki:
    def __init__(self, nimi: str, laji: str, syntymavuosi: int):
        self.nimi = nimi
        self.laji = laji
        self.syntymavuosi = syntymavuosi

def uusi_lemmikki(nimi: str, laji: str, syntymavuosi: int):
    return Lemmikki(nimi, laji, syntymavuosi)

if __name__ == "__main__":
    musti = uusi_lemmikki("Musti", "koira", 2017)
    print(musti.nimi)
    print(musti.laji)
    print(musti.syntymavuosi)

#osa8-08 ÄLÄ MUUTA ALLA OLEVAA LUOKKAA Kirja
# Kirjoita ratkaisui Kirja-luokan jälkeen
"""
Make a function vanhempi_kirja(kirja1: Kirja, kirja2: Kirja) that gets two Kirjaobjects as parameters.
The function tells which of the books is the older.
"""
class Kirja:
    def __init__(self, nimi: str, kirjoittaja: str, genre: str, kirjoitusvuosi: int):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre
        self.kirjoitusvuosi = kirjoitusvuosi

# -----------------------------
# tee ratkaisu tänne
def vanhempi_kirja(kirja1: Kirja, kirja2: Kirja):    
    if kirja1.kirjoitusvuosi < kirja2.kirjoitusvuosi:
        print(f"{kirja1.nimi} on vanhempi, se kirjoitettiin {kirja1.kirjoitusvuosi}")
    elif kirja1.kirjoitusvuosi > kirja2.kirjoitusvuosi:
        print(f"{kirja2.nimi} on vanhempi, se kirjoitettiin {kirja2.kirjoitusvuosi}")
    else:
        print(f"{kirja1.nimi} ja {kirja2.nimi} kirjoitettiin {kirja1.kirjoitusvuosi}")

if __name__ == "__main__":
    python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
    everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
    norma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)

    vanhempi_kirja(python, everest)
    vanhempi_kirja(python, norma)

#osa8-09 ÄLÄ MUUTA ALLA OLEVAA LUOKKAA Kirja
# Kirjoita ratkaisui Kirja-luokan jälkeen
"""
Make a function genren_kirjat(kirjat: list, genre: str) that gets a list Kirja object as a parameter and a string that tells the genre.
The function returns a new list to which it puts the books with the desired genre from the books in the parameter.
"""
class Kirja:
    def __init__(self, nimi: str, kirjoittaja: str, genre: str, kirjoitusvuosi: int):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre
        self.kirjoitusvuosi = kirjoitusvuosi

    # Tämä mahdollistaa kirjaolion järkevän tulostamisen print-funktiolla
    def __repr__(self):
        return f"{self.nimi} ({self.kirjoittaja}), {self.kirjoitusvuosi} - genre: {self.genre}"

# -----------------------------
# tee ratkaisu tänne
def genren_kirjat(kirjat: list, genre: str):
    target_list = []
    for item in kirjat:
        if item.genre == genre:
            target_list.append(item)
    return target_list

if __name__ == "__main__":
    python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
    everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
    norma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)

    kirjat = [python, everest, norma, Kirja("Lumiukko", "Jo Nesbø", "rikos", 2007)]

    print("rikoskirjoja ovat")
    for kirja in genren_kirjat(kirjat, "rikos"):
        print(f"{kirja.kirjoittaja}: {kirja.nimi}")

#osa8-10 Tee ratkaisusi tähän:
"""
- Make a method for the counter vahenna() that reduces the value of the object variable of the object being called by one,
but the conter never goes negative, if the counter value is already 0, it is no longer subtracted.
- Make a method for the counter nollaa() that resets the counter value.
- Make a method for the counter palauta_alkuperainen_arvo() that returns the original value to the counter.
"""
class VahenevaLaskuri:
    def __init__(self, arvo_alussa: int):
        self.arvo = arvo_alussa
        self.original_value = arvo_alussa

    def palauta_alkuperainen_arvo(self):
        self.arvo = self.original_value

    def tulosta_arvo(self):
        print("arvo:", self.arvo)

    def vahenna(self):
        if self.arvo >= 1:
            self.arvo = self.arvo - 1
        else:
            self.arvo = 0

    def nollaa(self):
        self.arvo = 0

if __name__ == "__main__":
    laskuri = VahenevaLaskuri(55)
    laskuri.vahenna()
    laskuri.vahenna()
    laskuri.vahenna()
    laskuri.vahenna()
    laskuri.tulosta_arvo()
    laskuri.palauta_alkuperainen_arvo()
    laskuri.tulosta_arvo()