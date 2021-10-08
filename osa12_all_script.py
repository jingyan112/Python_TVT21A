#osa12-1
"""
Implement the function jarjesta_varastosaldon_mukaan(alkiot: list) to sort the list according to third element of the tuple
Assign a ordering function to the ordering key of the sorted function.
Note: The key is a function that tells you how to determine the value of an individual item.

Output:
appelsiini 2 kpl
omena 3 kpl
banaani 12 kpl
vesimeloni 22 kpl
"""
def jarjesta_varastosaldon_mukaan(tuotteet: list):
    def tuple_item(tuple_item: tuple):
        return tuple_item[2]
    return sorted(tuotteet, key = tuple_item)

if __name__ == "__main__":
    tuotteet = [("banaani", 5.95, 12), ("omena", 3.95, 3), ("appelsiini", 4.50, 2), ("vesimeloni", 4.95, 22)]
    for tuote in jarjesta_varastosaldon_mukaan(tuotteet):
        print(f"{tuote[0]} {tuote[2]} kpl")

#osa12-2
"""
Implement the function jarjesta_tuotantokausien_mukaan(alkiot: list) to sort the list according to the "kausia" key in the dictionary
Assign a ordering function to the ordering key of the sorted function.
Note: The key is a function that tells you how to determine the value of an individual item.

Output:
Dexter  9 tuotantokautta
Friends  10 tuotantokautta
Simpsons  32 tuotantokautta
"""
def jarjesta_tuotantokausien_mukaan(alkiot: list):
    def dic_item(dic_item: dict):
        return dic_item["kausia"]
    return sorted(alkiot, key = dic_item)

if __name__ == "__main__":
    sarjat = [{ "nimi": "Dexter", "pisteet" : 8.6, "kausia":9 }, { "nimi": "Friends", "pisteet" : 8.9, "kausia":10 }, { "nimi": "Simpsons", "pisteet" : 8.7, "kausia":32 }]
    for sarja in jarjesta_tuotantokausien_mukaan(sarjat):
        print(f"{sarja['nimi']}  {sarja['kausia']} tuotantokautta")

#osa12-3
"""
Implement the function jarjesta_tuotantokausien_mukaan(alkiot: list) to sort the list according to the "pisteet" key in the dictionary descendingly
Assign a ordering function to the ordering key of the sorted function.
Note: The key is a function that tells you how to determine the value of an individual item.

Output:
IMDB:n mukainen pistemäärä
Friends  8.9
Simpsons  8.7
Dexter  8.6
"""
def jarjesta_pisteiden_mukaan(alkiot: list):
    def dic_item(dic_item: dict):
        return dic_item["pisteet"]
    return sorted(alkiot, key = dic_item, reverse = True)

if __name__ == "__main__":
    sarjat = [{ "nimi": "Dexter", "" : 8.6, "kausia":9 }, { "nimi": "Friends", "pisteet" : 8.9, "kausia":10 }, { "nimi": "Simpsons", "pisteet" : 8.7, "kausia":32 }]
    print("IMDB:n mukainen pistemäärä")
    for sarja in jarjesta_pisteiden_mukaan(sarjat):
        print(f"{sarja['nimi']}  {sarja['pisteet']}")

#osa12-4
"""
Implement pituuden_mukaan(reitit: list) to sort the list based on the pituus attribute of the class descendingly.
Implement vaikeuden_mukaan(reitit: list) to sort the list based on the grade attribute of the class descendingly,
if the grades are same, then based on the pituus attribute of the class descendingly.

Output:
Kantti, pituus 38 metriä, grade 6A+
Syncro, pituus 14 metriä, grade 8C+
Pieniä askelia, pituus 12 metriä, grade 6A+
Smooth operator, pituus 11 metriä, grade 7A

Syncro, pituus 14 metriä, grade 8C+
Smooth operator, pituus 11 metriä, grade 7A
Kantti, pituus 38 metriä, grade 6A+
Pieniä askelia, pituus 12 metriä, grade 6A+
"""
class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}"

def pituuden_mukaan(reitit: list):
    def class_item(class_item: Kiipeilyreitti):
        return class_item.pituus
    return sorted(reitit, key = class_item, reverse = True)

def vaikeuden_mukaan(reitit: list):
    def class_item(class_item: Kiipeilyreitti):
        return (class_item.grade, class_item.pituus)
    return sorted(reitit, key = class_item, reverse = True)

if __name__ == "__main__":
    r1 = Kiipeilyreitti("Kantti", 38, "6A+")
    r2 = Kiipeilyreitti("Smooth operator", 11, "7A")
    r3 = Kiipeilyreitti("Syncro", 14, "8C+")
    r4 = Kiipeilyreitti("Pieniä askelia", 12, "6A+")

    reitit = [r1, r2, r3, r4]

    for reitti in pituuden_mukaan(reitit):
        print(reitti)
    print()
    for reitti in vaikeuden_mukaan(reitit):
        print(reitti)

#osa12-5
"""
Given the following 2 class describing the climbing route: name of the route, length, difficulty level
Implement a function reittien_maaran_mukaan that sort the climbing cliffs in ascending order according to the number of routes.
Implement a function vaikeimman_reitin_mukaan that sort the climbing cliffs in descending order of the difficulty level.

Output:
Nummi 1 reittiä, vaikein 8C+
Olhava 3 reittiä, vaikein 6B
Nalkkilan släbi 4 reittiä, vaikein 7A

Nummi 1 reittiä, vaikein 8C+
Nalkkilan släbi 4 reittiä, vaikein 7A
Olhava 3 reittiä, vaikein 6B
"""
class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}"

class Kiipeilykallio:
    def __init__(self, nimi: str):
        self.nimi = nimi
        self.__reitit = []

    def lisaa_reitti(self, reitti: Kiipeilyreitti):
        self.__reitit.append(reitti)

    def reitteja(self):
        return len(self.__reitit)

    def vaikein_reitti(self):
        def vaikeuden_mukaan(reitti):
            return reitti.grade
        reitit_jarjestyksessa = sorted(self.__reitit, key=vaikeuden_mukaan)
        return reitit_jarjestyksessa[-1]

    def __str__(self):
        vaikein_reitti = self.vaikein_reitti()
        return f"{self.nimi} {self.reitteja()} reittiä, vaikein {vaikein_reitti.grade}"

def reittien_maaran_mukaan(kalliot: list):
    def class_item(class_item: Kiipeilykallio):
        return class_item.reitteja()
    return sorted(kalliot, key = class_item)

def vaikeimman_reitin_mukaan(kalliot: list):
    def class_item(class_item: Kiipeilykallio):
        return class_item.vaikein_reitti().grade
    return sorted(kalliot, key = class_item, reverse = True)

if __name__ == "__main__":
    k1 = Kiipeilykallio("Olhava")
    k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
    k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
    k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

    k2 = Kiipeilykallio("Nummi")
    k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))

    k3 = Kiipeilykallio("Nalkkilan släbi")
    k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))
    k3.lisaa_reitti(Kiipeilyreitti("Smooth operator", 11, "7A"))
    k3.lisaa_reitti(Kiipeilyreitti("Possu ei pidä", 12 , "6B+"))
    k3.lisaa_reitti(Kiipeilyreitti("Hedelmätarha", 8, "6A"))

    kalliot = [k1, k2, k3]
    for kallio in reittien_maaran_mukaan(kalliot):
        print(kallio)
    print()

    for kallio in vaikeimman_reitin_mukaan(kalliot):
        print(kallio)

#osa12-6
"""
Given the class Palloilija describing ball player: name, number, goals, entries, minutes of play
Using lambda method to:
- Implement eniten_maaleja(joukkue: list) which returns the player name with highest maalit
- Implement eniten_pisteita(joukkue: list) which returns the player name and player number with highest sum of maalit and goals
- Implement vahiten_minuutteja(joukkue: list) which returns the class of the player with least minutes of play

Output:
Kelju Kojootti
('Uka Naakka', 9)
Palloilija(nimi=Hessu Hopo, pelinumero=4, maalit=3, syotot=9, minuutit=12)
"""
class Palloilija:
    def __init__(self, nimi: str, pelinumero: int, maalit: int, syotot: int, minuutit: int):
        self.nimi = nimi
        self.pelinumero = pelinumero
        self.maalit = maalit
        self.syotot = syotot
        self.minuutit = minuutit

    def __str__(self):
        return (f'Palloilija(nimi={self.nimi}, pelinumero={self.pelinumero}, '
            f'maalit={self.maalit}, syotot={self.syotot}, minuutit={self.minuutit})')

def eniten_maaleja(joukkue: list):
    return sorted(joukkue, key=lambda class_item: class_item.maalit)[-1].nimi

def eniten_pisteita(joukkue: list):
    result = sorted(joukkue, key=lambda class_item: class_item.maalit + class_item.syotot)[-1]
    return (result.nimi, result.pelinumero)

def vahiten_minuutteja(joukkue: list):
    return sorted(joukkue, key=lambda class_item: class_item.minuutit)[0]

if __name__ == "__main__":
    pelaaja1 = Palloilija("Kelju Kojootti", 13, 5, 12, 46)
    pelaaja2 = Palloilija("Maantiekiitäjä", 7, 2, 26, 55)
    pelaaja3 = Palloilija("Uka Naakka", 9, 1, 32, 26)
    pelaaja4 = Palloilija("Pelle Peloton", 12, 1, 11, 41)
    pelaaja5 = Palloilija("Hessu Hopo", 4, 3, 9, 12)
    joukkue = [pelaaja1, pelaaja2, pelaaja3, pelaaja4, pelaaja5]
    print(eniten_maaleja(joukkue))
    print(eniten_pisteita(joukkue))
    print(vahiten_minuutteja(joukkue))