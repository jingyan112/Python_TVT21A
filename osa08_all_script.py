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

#osa8-10b Tee ratkaisusi tähän:
"""
Write a class Henkilo that has only one attribute nimi that is set in the constructor.
In addition, two methods should be written for the class:
- The method anna_etunimi returns the person's first name and the method anna_sukunim returns the person's last name irespectively.
You can assume in the methods that the name given in the constructs has a first and last name separated by a space and no other names.
"""
class Henkilo:
    def __init__(self, nimi: str):
        self.nimi = nimi
    
    def anna_etunimi(self):
        return self.nimi.split(" ")[0]
    
    def anna_sukunimi(self):
        return self.nimi.split(" ")[1]
    
if __name__ == "__main__":
    pekka = Henkilo("Pekka Python")
    print(pekka.anna_etunimi())
    print(pekka.anna_sukunimi())

    pauli = Henkilo("Pauli Pythonen")
    print(pauli.anna_etunimi())
    print(pauli.anna_sukunimi())

#osa8-11 Tee ratkaisusi tähän:
"""
Make a class Lukutilasto that knows the following functions:
- the method lisaa_luku adds a new number to the statistic
- the method lukujen_maara tells you the number of numbers added
- the method summa tells the sum of the added numbers (the sum of the empty number statistics is 0)
- the method keskiarvo tells the average of the added numbers (the average of the empty number statistic is 0)
"""
class  Lukutilasto:
    def __init__(self):
        self.counterlist = []

    def lisaa_luku(self, luku:int):
        self.counterlist.append(luku)

    def lukujen_maara(self):
        return len(self.counterlist)

    def summa(self):
        if len(self.counterlist) == 0:
            return 0
        else:
            return sum(self.counterlist)

    def keskiarvo(self):
        if len(self.counterlist) == 0:
            return 0
        else:
            return sum(self.counterlist)/len(self.counterlist)
    
    def summa_even(self):
        summa_even = 0

        for item in self.counterlist:
            if item % 2 == 0:
                summa_even = summa_even + item
        
        return summa_even

    def summa_odd(self):
        summa_odd = 0

        for item in self.counterlist:
            if item % 2 == 1:
                summa_odd = summa_odd + item
        
        return summa_odd

tilasto = Lukutilasto()
print("Anna lukuja:")

while True:
    num = int(input())
    if num == -1:
        break
    else:
        tilasto.lisaa_luku(num)

print("Summa:", tilasto.summa())
print("Keskiarvo:", tilasto.keskiarvo())
print("Parillisten summa:", tilasto.summa_even())
print("Parittomien summa:", tilasto.summa_odd())

#osa8-11a Tee ratkaisusi tähän:
"""
Implement a class Sekuntikello that prints minute:second through __str__ method.
In addition, the method tick takes the clock one second forward, and the value of both seconds and minutes is at most 59

00:00
00:01
00:02
...
59:58
59:59
00:00
00:01
"""
class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0

    def __str__(self):
        if self.sekunnit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if self.minuutit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return f"0{self.minuutit}:0{self.sekunnit}"
            else:
                return f"{self.minuutit}:0{self.sekunnit}"
        else:
            if self.minuutit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return f"0{self.minuutit}:{self.sekunnit}"
            else:
                return f"{self.minuutit}:{self.sekunnit}" 

    def tick(self):
        self.sekunnit = self.sekunnit + 1
        if self.sekunnit == 60:
            self.sekunnit = 0
            self.minuutit = self.minuutit + 1
        if self.minuutit == 60:
            self.minuutit = 0

if __name__ == "__main__":
    kello = Sekuntikello()
    for i in range(3600):
        print(kello)
        kello.tick()

#osa8-12 Tee ratkaisusi tähän:
"""
Implement a class Kello that prints hour:minute:second through __str__ method.
In addition,  the method tick takes the clock one second forward, and the value of both seconds and minutes is at most 59, and the value of hours is at most 24.
Furthermore, the method aseta will reset the time with new values of hours and minutes, the value for seconds will be 0.
Output for the main function:

23:59:55
23:59:56
23:59:57
23:59:58
23:59:59
00:00:00
00:00:01
12:05:00
"""
class Kello:
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        if self.second in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if self.minute in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if self.hour in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    return f"0{self.hour}:0{self.minute}:0{self.second}"
                else:
                    return f"{self.hour}:0{self.minute}:0{self.second}"
            else:
                if self.hour in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    return f"0{self.hour}:{self.minute}:0{self.second}"
                else:
                    return f"{self.hour}:{self.minute}:0{self.second}"
        else:
            if self.minute in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if self.hour in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    return f"0{self.hour}:0{self.minute}:{self.second}"
                else:
                    return f"{self.hour}:0{self.minute}:{self.second}"
            else:
                if self.hour in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    return f"0{self.hour}:{self.minute}:{self.second}"
                else:
                    return f"{self.hour}:{self.minute}:{self.second}"                   

    def tick(self):
        self.second = self.second + 1
        if self.second == 60:
            self.second = 0
            self.minute = self.minute + 1
        if self.minute == 60:
            self.minute = 0
            self.hour = self.hour + 1
        if self.hour == 24:
            self.hour = 0
    
    def aseta(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute
        self.second = 0

if __name__ == "__main__":
    kello = Kello(23, 59, 55)
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.aseta(12, 5)
    print(kello)

#osa8-13 Tee ratkaisusi tähän:
"""
Implement Maksukortti class with the following methods:
- __str__method that returns the card balance in the form "The card has money X euros".
- syo_edullisesti method which reduces the card balance by 2.60 euros,
the card balance will no longer decrease if the balance is insufficient when paying
- syo_maukkaasti method which reduces the card balance by 4.60 euros,
the card balance will no longer decrease if the balance is insufficient when paying
- lataa_rahaa method which increase the card balance by the amount of money given by the parameter,
and will raise an error if the given value is negative

Plus, implement the program to output the following infomation:
Pekka: Kortilla on rahaa 15.4 euroa
Matti: Kortilla on rahaa 27.4 euroa
Pekka: Kortilla on rahaa 35.4 euroa
Matti: Kortilla on rahaa 22.8 euroa
Pekka: Kortilla on rahaa 30.2 euroa
Matti: Kortilla on rahaa 72.8 euroa
"""
class Maksukortti:
    def __init__(self, alkusaldo: float):
        self.saldo = alkusaldo

    def __str__(self):
        return "Kortilla on rahaa {:.1f} euroa".format(self.saldo)
    
    def syo_edullisesti(self):
        if self.saldo >= 2.60:
            self.saldo = self.saldo - 2.60
    
    def syo_maukkaasti(self):
        if self.saldo >= 4.60:
            self.saldo = self.saldo - 4.60
    
    def lataa_rahaa(self, increasing_value: float):
        if increasing_value >= 0:
            self.saldo = self.saldo + increasing_value
        else:
            raise ValueError("Kortille ei saa ladata negatiivista summaa")
    
pekan_kortti = Maksukortti(20)
matin_kortti = Maksukortti(30)
pekan_kortti.syo_maukkaasti()
print("Pekka:", pekan_kortti)
matin_kortti.syo_edullisesti()
print("Matti:", matin_kortti)
pekan_kortti.lataa_rahaa(20)
print("Pekka:", pekan_kortti)
matin_kortti.syo_maukkaasti()
print("Matti:", matin_kortti)
pekan_kortti.syo_edullisesti()
pekan_kortti.syo_edullisesti()
print("Pekka:", pekan_kortti)
matin_kortti.lataa_rahaa(50)
print("Matti:", matin_kortti)