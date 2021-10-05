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