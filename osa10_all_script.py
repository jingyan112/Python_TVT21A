#osa10-1
"""
Defines Tietokone class with the attributes malliand nopeus.
Make KannettavaTietokone class that inherits the class Computer.
In addition to the attributes of Tietokone, the class gets a third integer type attribute in the constructor paino.
In addition, write a method in the class __str__that allows you to print a printout of the state of the object
according to the example embodiment.
"""
class Tietokone:
    def __init__(self, malli: str, nopeus: int):
        self.__malli = malli
        self.__nopeus = nopeus

    def malli(self):
        return self.__malli

    def nopeus(self):
        return self.__nopeus

class KannettavaTietokone(Tietokone):
    def __init__(self, malli: str, nopeus: int, paino: int):
        super().__init__(malli, nopeus)
        self.__paino = paino
    
    def paino(self):
        return self.__paino
    
    def __str__(self):
        return "{}, {} MHz, {} kg".format(super().malli(), super().nopeus(), self.paino())

if __name__ == "__main__":
    ipm = KannettavaTietokone("IPM MikroMauri", 1500, 2)
    print(ipm)  # IPM MikroMauri, 1500 MHz, 2 kg

#osa10-2
"""
Make Pelimuseo class inherits the Pelivarasto class.
In the Game Museum category, the method is re-implemented anna_pelit()
so that it returns only games made before 1990 to the list.
In addition, the class must have a constructor called the superclass Game Store constructor.
The constructor has no parameters.
"""
class Tietokonepeli:
    def __init__(self, nimi: str, julkaisija: str, vuosi: int):
        self.nimi = nimi
        self.julkaisija = julkaisija
        self.vuosi = vuosi

class Pelivarasto:
    def __init__(self):
        self.__pelit = []

    def lisaa_peli(self, peli: Tietokonepeli):
        self.__pelit.append(peli)

    def anna_pelit(self):
        return self.__pelit

class Pelimuseo(Pelivarasto):
    def __init__(self):
        super().__init__()
    
    def lisaa_peli(self, peli: Tietokonepeli):
        super().lisaa_peli(peli)
    
    def anna_pelit(self):
        proper_game_list = []
        for game in super().anna_pelit():
            if game.vuosi <= 1990:
                proper_game_list.append(game)
        return proper_game_list

if __name__ == "__main__":
    museo = Pelimuseo()
    museo.lisaa_peli(Tietokonepeli("Pacman", "Namco", 1980))
    museo.lisaa_peli(Tietokonepeli("GTA 2", "Rockstar", 1999))
    museo.lisaa_peli(Tietokonepeli("Bubble Bobble", "Taito", 1986))
    for peli in museo.anna_pelit():
        print(peli.nimi)    
# Output:
# Pacman
# Bubble Bobble

#osa10-3
"""
Implement a class Nelio that inherits the class Suorakulmio.
Unlike rectangle square all sides are the same length, that is,
the square is a kind of simpler special case of a rectangle.
The class must not define new attributes!
"""
class Suorakulmio:
    def __init__(self, leveys: int, korkeus: int):
        self.leveys = leveys
        self.korkeus = korkeus

    def __str__(self):
        return f"suorakulmio {self.leveys}x{self.korkeus}"

    def pinta_ala(self):
        return self.leveys * self.korkeus

class Nelio(Suorakulmio):
    def __init__(self, side_length: int):
        super().__init__(side_length, side_length)
    
    def __str__(self):
        return "neliö {}x{}".format(self.leveys, self.korkeus)
    
    def pinta_ala(self):
        super().pinta_ala()
        return self.leveys * self.korkeus

if __name__ == "__main__":
    suorakulmio = Suorakulmio(2, 3)
    print(suorakulmio)                              # suorakulmio 2x3
    print("pinta-ala:", suorakulmio.pinta_ala())    # pinta-ala: 6

    nelio = Nelio(4)
    print(nelio)                                    # neliö  4x4
    print("pinta-ala:", nelio.pinta_ala())          # pinta-ala: 16

#osa10-4
"""
Implement class PisinSana that inherits from class Sanapeli, which returns the winner with the longest word
Implement class EnitenVokaaleja that inherits from class Sanapeli, which returns the winner with more vowels in the word
Implement class KiviPaperiSakset that inherits from class Sanapeli,which returns the winner following stone, paper and scissors rules
(Rock, Paper, Scissors) = (kivi, paperi, sakset)
"""
import random

class Sanapeli():
    def __init__(self, kierrokset: int):
        self.voitot1 = 0
        self.voitot2 = 0
        self.kierrokset = kierrokset

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # arvotaan voittaja
        return random.randint(1, 2)

    def pelaa(self):
        print("Sanapeli:")
        for i in range(1, self.kierrokset+1):
            print(f"kierros {i}")
            vastaus1 = input("pelaaja1: ")
            vastaus2 = input("pelaaja2: ")

            if self.kierroksen_voittaja(vastaus1, vastaus2) == 1:
                self.voitot1 += 1
                print("pelaaja 1 voitti")
            elif self.kierroksen_voittaja(vastaus1, vastaus2) == 2:
                self.voitot2 += 1
                print("pelaaja 2 voitti")
            else:
                pass # tasapeli

        print("peli päättyi, voitot:")
        print(f"pelaaja 1: {self.voitot1}")
        print(f"pelaaja 2: {self.voitot2}")

class PisinSana(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        if len(pelaaja1_sana) > len(pelaaja2_sana):
            return 1
        elif len(pelaaja1_sana) < len(pelaaja2_sana):
            return 2
        else:
            pass

class EnitenVokaaleja(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        counter1 = pelaaja1_sana.count('ä') + pelaaja1_sana.count('a') + pelaaja1_sana.count('å') + pelaaja1_sana.count('e') + pelaaja1_sana.count('i') + pelaaja1_sana.count('o') + pelaaja1_sana.count('ö') + pelaaja1_sana.count('u') + pelaaja1_sana.count('y')
        counter2 = pelaaja2_sana.count('ä') + pelaaja2_sana.count('a') + pelaaja2_sana.count('å') + pelaaja2_sana.count('e') + pelaaja2_sana.count('i') + pelaaja2_sana.count('o') + pelaaja2_sana.count('ö') + pelaaja2_sana.count('u') + pelaaja2_sana.count('y')
        if counter1 > counter2:
            return 1
        elif counter1 < counter2:
            return 2
        else:
            pass

class KiviPaperiSakset(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)
    
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        if pelaaja1_sana in ["kivi", "paperi", "sakset"] and pelaaja2_sana in ["kivi", "paperi", "sakset"]:
            if pelaaja1_sana == "kivi":         # rock
                if pelaaja2_sana == "paperi":
                    return 2
                elif pelaaja2_sana == "sakset":
                    return 1
                else:
                    pass
            elif pelaaja1_sana == "paperi":     # paper
                if pelaaja2_sana == "kivi":
                    return 1
                elif pelaaja2_sana == "sakset":
                    return 2
                else:
                    pass
            elif pelaaja1_sana == "sakset":     # scissors
                if pelaaja2_sana == "kivi":
                    return 2
                elif pelaaja2_sana == "paperi":
                    return 1
                else:
                    pass
            else:
                pass
        elif pelaaja1_sana in ["kivi", "paperi", "sakset"] and pelaaja2_sana not in ["kivi", "paperi", "sakset"]:
            return 1
        elif pelaaja1_sana not in ["kivi", "paperi", "sakset"] and pelaaja2_sana in ["kivi", "paperi", "sakset"]:
            return 2
        else:
            pass



if __name__ == "__main__":
    p = KiviPaperiSakset(3)
    p.pelaa()

"""
Example:
yanjing@yanjingdeMacBook-Pro src % cd /Users/yanjing/Downloads/osa10/*/src; python3 *.py
Sanapeli:
kierros 1
pelaaja1: kivi
pelaaja2: laiva
pelaaja 1 voitti
kierros 2
pelaaja1: dynamiitti
pelaaja2: sakset
pelaaja 2 voitti
kierros 3
pelaaja1: auto
pelaaja2: mopo
peli päättyi, voitot:
pelaaja 1: 1
pelaaja 2: 1
"""

#osa10-5
"""
A class is ready in the task template SuperSankari.
Write a class SuperRyhma that models a group of superheroes.
The class must have the following characteristics:
- Protected attributes name (string), domicile (string) and members (list)
- A constructor that gets its name and domicile as its parameter in this order
- Detection methods for name and domicile
- A method lisaa_jasen(sankari: SuperSankari)that adds a new member to a group
- A method tulosta_ryhmathat prints the information for a group and its members according to the example below

Expected output:
Output:
Ryhmä Z, Kälviä
Jäsenet:
Supermiekkonen, superkyvyt: Supernopeus, supervoimakkuus
Näkymätön Makkonen, superkyvyt: Näkymättömyys
"""
class SuperSankari:
    def __init__(self, nimi: str, supervoimat: str):
        self.nimi = nimi
        self.supervoimat = supervoimat

    def __str__(self):
        return f'{self.nimi}, superkyvyt: {self.supervoimat}'

class SuperRyhma():
    def __init__(self, nimi: str, kotipaikka: str):
        self._nimi = nimi
        self._kotipaikka = kotipaikka
        self._jasenet = []
    
    def nimi(self):
        return self._nimi
    
    def kotipaikka(self):
        return self._kotipaikka
    
    def lisaa_jasen(self, sankari: SuperSankari):
        self._jasenet.append(sankari)
    
    def tulosta_ryhma(self):
        print("{}, {}".format(self.nimi(), self.kotipaikka()))
        print("Jäsenet:")
        for element in self._jasenet:
            print("{}, superkyvyt: {}".format(element.nimi, element.supervoimat))

if __name__ == "__main__":
    supermiekkonen = SuperSankari("Supermiekkonen", "Supernopeus, supervoimakkuus")
    nakymaton = SuperSankari("Näkymätön Makkonen", "Näkymättömyys")
    ryhma_z = SuperRyhma("Ryhmä Z", "Kälviä")

    ryhma_z.lisaa_jasen(supermiekkonen)
    ryhma_z.lisaa_jasen(nakymaton)
    ryhma_z.tulosta_ryhma()

#osa10-6
"""
Implement SalainenTaikajuoma class that inherits from Taikajuoma class with the following characteristics:
- SalainenTaikajuoma class receives a password (salasana) in the constructor.
- The method lisaa_aines(ainesosa: str, maara: float, salasana: str) can be only called successfully with right password, otherwise, will raise ValueError exception.
- The method tulosta_resepti(salasana: str) can be only called successfully with right password, otherwise, will raise ValueError exception.

Expected output:
yanjing@yanjingdeMacBook-Pro src % cd /Users/yanjing/Downloads/osa10/*/src; python3 *.py
Kutistus maksimus:
Kärpässieni 1.5 grammaa
Taikahiekka 3.0 grammaa
Sammakonkutu 4.0 grammaa
Traceback (most recent call last):
  File "salainen_taikajuoma.py", line 41, in <module>
    kutistus.lisaa_aines("Sammakonkutuhhhhhh", 8.0, "hokkuspokkussss")
  File "salainen_taikajuoma.py", line 27, in lisaa_aines
    raise ValueError("Väärä salasana!")
ValueError: Väärä salasana!
"""
class Taikajuoma:
    def __init__(self, nimi: str):
        self._nimi = nimi
        self._ainekset = []

    def lisaa_aines(self, ainesosa: str, maara: float):
        self._ainekset.append((ainesosa, maara))

    def tulosta_resepti(self):
        print(self._nimi + ":")
        for aines in self._ainekset:
            print(f"{aines[0]} {aines[1]} grammaa")

class SalainenTaikajuoma(Taikajuoma):
    def __init__(self, nimi: str, salasana: str):
        super().__init__(nimi)
        self._salasana = salasana
    
    def salasana(self):
        return self._salasana
    
    def lisaa_aines(self, ainesosa: str, maara: float, salasana: str):
        if self.salasana() == salasana:
            super().lisaa_aines(ainesosa, maara)
        else:
            raise ValueError("Väärä salasana!")

    def tulosta_resepti(self, salasana: str):
        if self.salasana() == salasana:
            super().tulosta_resepti()
        else:
            raise ValueError("Väärä salasana!")

if __name__ == "__main__":
    kutistus = SalainenTaikajuoma("Kutistus maksimus", "hokkuspokkus")
    kutistus.lisaa_aines("Kärpässieni", 1.5, "hokkuspokkus")
    kutistus.lisaa_aines("Taikahiekka", 3.0, "hokkuspokkus")
    kutistus.lisaa_aines("Sammakonkutu", 4.0, "hokkuspokkus")
    kutistus.tulosta_resepti("hokkuspokkus")
    kutistus.lisaa_aines("Sammakonkutuhhhhhh", 8.0, "hokkuspokkussss")
    kutistus.tulosta_resepti("pokkushokkus") # VÄÄRÄ SALASANA!

#osa10-7
"""
Implement the following methods for Raha class:
- __init__(self) method to construct the integer and decimal part of the money
- __str__(self) method to make sure the value of money is printed in the right format
- __eq__, __lt__, __gt__, __ne__ to compare the two different amounts of money
- __add__, __sub__ to operate  the two different amounts of money, and return the object

Expected output:
7.70 eur
1.80 eur
Traceback (most recent call last):
  File "raha.py", line 58, in <module>
    e5 = e2-e1
  File "raha.py", line 46, in __sub__
    raise ValueError("negatiivinen tulos ei sallittu")
ValueError: negatiivinen tulos ei sallittu
"""
class Raha:
    def __init__(self, eurot: int, sentit: int):
        self._eurot = eurot
        self._sentit = sentit

    def __str__(self):
        if self._sentit < 10:
            return f"{self._eurot}.0{self._sentit} eur"
        else:
            return f"{self._eurot}.{self._sentit} eur"

    def __repr__(self):
        if self._sentit < 10:
            return float("{}.0{}".format(self._eurot, self._sentit))
        else:
            return float("{}.{}".format(self._eurot, self._sentit))

    def __eq__(self, toinen):
        return self.__repr__() == toinen.__repr__()
    
    def __lt__(self, toinen):
        return self.__repr__() < toinen.__repr__()
    
    def __gt__(self, toinen):
        return self.__repr__() > toinen.__repr__()
    
    def __ne__(self, toinen):
        return self.__repr__() != toinen.__repr__()
    
    def __add__(self, toinen):
        result = round(self.__repr__() + toinen.__repr__(), 2)
        add_result = Raha(0, 0)
        add_result._eurot = int(result)
        add_result._sentit = int(round(result - add_result._eurot, 2) * 100)
        return add_result

    def __sub__(self, toinen):
        result = round(self.__repr__() - toinen.__repr__(), 2)
        if result >= 0:
            sub_result = Raha(0, 0)
            sub_result._eurot = int(result)
            sub_result._sentit = int(round(result - sub_result._eurot, 2) * 100)
            return sub_result
        else:
            raise ValueError("negatiivinen tulos ei sallittu")

if __name__ == "__main__":
    e1 = Raha(4, 75)
    e2 = Raha(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1

#osa10-8
"""
Implement Paivays class with the following characteristics:
- makes it possible to handle dates, but do not use datetime module, and assume every month has 30 days
- Implement the class body and its comparison operators <,>, == and! =
- Implement operator + for the date, and do not change the original date
- Implement an operator for the date that returns the difference in dates in days
"""
class Paivays:
    def __init__(self, date: int, month: int, year: int):
        self.date = date
        self.month = month
        self.year = year
    
    def __str__(self):
        return "{}.{}.{}".format(self.date, self.month, self.year)

    def __repr__(self):
        if self.date >= 10:
            if self.month >= 10:
                return "{}{}{}".format(self.year, self.month, self.date)
            else:
                return "{}0{}{}".format(self.year, self.month, self.date)
        else:
            if self.month >= 10:
                return "{}{}0{}".format(self.year, self.month, self.date)
            else:
                return "{}0{}0{}".format(self.year, self.month, self.date)
            
    def __eq__(self, toinen):
        return int(self.__repr__()) == int(toinen.__repr__())
    
    def __lt__(self, toinen):
        return int(self.__repr__()) < int(toinen.__repr__())
    
    def __gt__(self, toinen):
        return int(self.__repr__()) > int(toinen.__repr__())
    
    def __ne__(self, toinen):
        return int(self.__repr__()) != int(toinen.__repr__())
    
    # Assume every month has 30 days
    def __add__(self, days: int):
        new_date = Paivays(0, 0, 0)
        new_date.year = self.year + days//360
        new_date.month = self.month + days%360//30
        new_date.date = self.date + days%360%30
        if new_date.date > 30:
            new_date.date = new_date.date - 30
            new_date.month = new_date.month + 1
        if new_date.month > 12:
            new_date.month = new_date.month - 12
            new_date.year = new_date.year + 1
        return new_date
    
    def __sub__(self, dateb):
        return abs((self.year-1)*360 + (self.month-1)*30 + self.date - (dateb.year-1)*360 - (dateb.month-1)*30 - dateb.date)

if __name__ == "__main__":
    pv1 = Paivays(19, 9, 1976)
    pv2 = Paivays(9, 10, 1976)
    print(pv2>pv1)              # True

#osa10-9
"""
Make the class Kauppalista iterable and the code block in main function can work properly
"""
class Kauppalista:
    def __init__(self):
        self.tuotteet = []

    def tuotteita(self):
        return len(self.tuotteet)

    def lisaa(self, tuote: str, maara: int):
        self.tuotteet.append((tuote, maara))

    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n < self.tuotteita():
            element = self.tuotteet[self.n]
            self.n += 1
            return element
        else:
            raise StopIteration    

if __name__ == "__main__":
    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("ananas", 1)

    for tuote in lista:
        print(f"{tuote[0]}: {tuote[1]} kpl")