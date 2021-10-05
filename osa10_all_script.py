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