# osa9-01
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
    return max(new_dic, key=new_dic.get)


if __name__ == "__main__":
    auto1 = Auto("Mersu", 195)
    auto2 = Auto("Lada", 110)
    auto3 = Auto("Ferrari", 280)
    auto4 = Auto("Trabant", 85)

    autot = [auto1, auto2, auto3, auto4]
    print(nopein_auto(autot))

# osa9-02
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


if __name__ == "__main__":
    s1 = Koesuoritus("Pekka", 12)
    s2 = Koesuoritus("Pirjo", 19)
    s3 = Koesuoritus("Pauli", 15)
    s4 = Koesuoritus("Pirkko", 9)
    s5 = Koesuoritus("Petriina", 17)

    hyv = hyvaksytyt([s1, s2, s3, s4, s5], 15)
    for hyvaksytty in hyv:
        print(hyvaksytty)

# osa9-03
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

# osa9-04
"""
In Maksukortti class:
- Implement lataa_rahaa(lisays) method that add the balance by lisays
- Implement ota_rahaa(maara) method that reduce the balance by maara, while the balance wont go negative.
If the balance is less than maara, return False, otherwise, return True.

In Kassapaate class:
- Implement syo_edullisesti(maksu) method to buy the cheap lunch (2.50e) with maksu cash, check whether the cash is enough
- Implement syo_maukkaasti(maksu) method to buy the expensive lunch (4.30e) with maksu cash, check whether the cash is enough
- Implement syo_edullisesti_kortilla(kortti) method to buy the cheap lunch (2.50e) with card, card info is stored in kortti:Maksukortti class
- Implement syo_maukkaasti_kortilla(kortti) method to buy the expensive lunch (4.30e) with card, card info is stored in kortti:Maksukortti class
- Implement lataa_rahaa_kortille(kortti, summa) method to top up the card with summa
- rahaa variable to record cash changes, the original value is 1000
- edulliset to record how many cheap lunches are sold
- maukkaat to record how many expensive lunches are sold
"""


class Maksukortti:
    def __init__(self, saldo: float):
        self.saldo = saldo  # The current balance

    def lataa_rahaa(self, lisays: float):  # Add the current balance by lisays
        self.saldo = self.saldo + lisays

    def ota_rahaa(self, maara: float):  # Reduce the current balance by maara
        if self.saldo >= maara:
            self.saldo = self.saldo - maara
            return True
        else:
            return False


class Kassapaate:
    def __init__(self):
        self.rahaa = 1000   # Cash changes
        self.edulliset = 0  # Calculate how many cheap lunches are sold
        self.maukkaat = 0   # Calculate how many expensive lunches are sold

    def syo_edullisesti(self, maksu: float):    # 2.50 for the cheap lunch, for cash
        if maksu >= 2.50:
            self.edulliset = self.edulliset + 1
            self.rahaa = self.rahaa + 2.50
            return maksu - 2.50
        else:
            return maksu

    # 4.30 for the expensive lunch, for cash
    def syo_maukkaasti(self, maksu: float):
        if maksu >= 4.30:
            self.maukkaat = self.maukkaat + 1
            self.rahaa = self.rahaa + 4.30
            return maksu - 4.30
        else:
            return maksu

    # 2.50 for the cheap lunch, for card
    def syo_edullisesti_kortilla(self, kortti: Maksukortti):
        if kortti.ota_rahaa(2.50):
            self.edulliset = self.edulliset + 1
            return True
        else:
            return False

    # 4.30 for the expensive lunch, for card
    def syo_maukkaasti_kortilla(self, kortti: Maksukortti):
        if kortti.ota_rahaa(4.30):
            self.maukkaat = self.maukkaat + 1
            return True
        else:
            return False

    def lataa_rahaa_kortille(self, kortti: Maksukortti, summa: float):
        self.rahaa = self.rahaa + summa
        return kortti.lataa_rahaa(summa)


if __name__ == "__main__":
    # test1
    kortti = Maksukortti(10)
    print("Rahaa", kortti.saldo)        # Rahaa 10
    tulos = kortti.ota_rahaa(8)
    print("Onnistuiko otto:", tulos)    # Onnistuiko otto: True
    print("Rahaa", kortti.saldo)        # Rahaa 2
    tulos = kortti.ota_rahaa(4)
    print("Onnistuiko otto:", tulos)    # Onnistuiko otto: False
    print("Rahaa", kortti.saldo)        # Rahaa 2
    exactum = Kassapaate()

    # test2
    exactum = Kassapaate()
    vaihtorahaa = exactum.syo_edullisesti(10)
    print("Vaihtorahaa jäi", vaihtorahaa)       # Vaihtorahaa jäi 7.5
    vaihtorahaa = exactum.syo_edullisesti(5)
    print("Vaihtorahaa jäi", vaihtorahaa)       # Vaihtorahaa jäi 2.5
    vaihtorahaa = exactum.syo_maukkaasti(4.3)
    print("Vaihtorahaa jäi", vaihtorahaa)       # Vaihtorahaa jäi 0.0
    # Kassassa rahaa 1009.3
    print("Kassassa rahaa", exactum.rahaa)
    # Edullisia lounaita myyty 2
    print("Edullisia lounaita myyty", exactum.edulliset)
    # Maukkaita lounaita myyty 1
    print("Maukkaita lounaita myyty", exactum.maukkaat)

    # test3
    exactum = Kassapaate()
    vaihtorahaa = exactum.syo_edullisesti(10)
    print("Vaihtorahaa jäi", vaihtorahaa)       # Vaihtorahaa jäi 7.5
    kortti = Maksukortti(7)
    tulos = exactum.syo_maukkaasti_kortilla(kortti)
    print("Riittikö raha:", tulos)              # Riittikö raha: True
    tulos = exactum.syo_maukkaasti_kortilla(kortti)
    print("Riittikö raha:", tulos)              # Riittikö raha: False
    tulos = exactum.syo_edullisesti_kortilla(kortti)
    print("Riittikö raha:", tulos)              # Riittikö raha: True
    print("Kassassa rahaa", exactum.rahaa)      # Kassassa rahaa 1002.5
    # Edullisia lounaita myyty 2
    print("Edullisia lounaita myyty", exactum.edulliset)
    # Maukkaita lounaita myyty 1
    print("Maukkaita lounaita myyty", exactum.maukkaat)

    # test4
    exactum = Kassapaate()
    antin_kortti = Maksukortti(2)
    # Kortilla rahaa 2 euroa
    print(f"Kortilla rahaa {antin_kortti.saldo} euroa")
    tulos = exactum.syo_maukkaasti_kortilla(antin_kortti)
    # Riittikö raha: False
    print("Riittikö raha:", tulos)
    exactum.lataa_rahaa_kortille(antin_kortti, 100)
    # Kortilla rahaa 102 euroa
    print(f"Kortilla rahaa {antin_kortti.saldo} euroa")
    tulos = exactum.syo_maukkaasti_kortilla(antin_kortti)
    # Riittikö raha: True
    print("Riittikö raha:", tulos)
    # Kortilla rahaa 97.7 euroa
    print(f"Kortilla rahaa {antin_kortti.saldo} euroa")
    # Kassassa rahaa 1100
    print("Kassassa rahaa", exactum.rahaa)
    # Edullisia lounaita myyty 0
    print("Edullisia lounaita myyty", exactum.edulliset)
    # Maukkaita lounaita myyty 1
    print("Maukkaita lounaita myyty", exactum.maukkaat)

# osa9-05
"""
Make a method suurempi(self, verrattava) that returns True if the dwelling object itself is larger in area than the comparable dwelling object.
Make a method hintaero(self, verrattava) that returns the price difference between a dwelling object and a comparable dwelling object. 
Make a method kalliimpi(self, verrattava) that returns Trueif the dwelling object is more expensive than the comparable dwelling object.
"""


class Asunto:
    def __init__(self, huoneita: int, nelioita: int, neliohinta: int):
        self.huoneita = huoneita
        self.nelioita = nelioita
        self.neliohinta = neliohinta

    def suurempi(self, verrattava):
        return self.nelioita > verrattava.nelioita

    def hintaero(self, verrattava):
        return abs(self.nelioita * self.neliohinta - verrattava.nelioita * verrattava.neliohinta)

    def kalliimpi(self, verrattava):
        return self.nelioita * self.neliohinta > verrattava.nelioita * verrattava.neliohinta


if __name__ == "__main__":
    eira_yksio = Asunto(1, 16, 5500)
    kallio_kaksio = Asunto(2, 38, 4200)
    jakomaki_kolmio = Asunto(3, 78, 2500)

    print(eira_yksio.suurempi(kallio_kaksio))       # False
    print(jakomaki_kolmio.suurempi(kallio_kaksio))  # True

    print(eira_yksio.hintaero(kallio_kaksio))       # 71600
    print(jakomaki_kolmio.hintaero(kallio_kaksio))  # 35400

    print(eira_yksio.kalliimpi(kallio_kaksio))      # False
    print(jakomaki_kolmio.kalliimpi(kallio_kaksio))  # True

# osa9-06
"""
Complete the class Henkilo method __str__so that the method returns a string that
tells the person's name in addition to the pet's name and breed under the sample printout.
"""


class Lemmikki:
    def __init__(self, nimi: str, kuvaus: str):
        self.nimi = nimi
        self.kuvaus = kuvaus

    def __str__(self):
        return f"{self.nimi} ({self.kuvaus})"


class Henkilo:
    def __init__(self, nimi: str, lemmikki: Lemmikki):
        self.nimi = nimi
        self.lemmikki = lemmikki

    def __str__(self):
        return f"{self.nimi}, kaverina {self.lemmikki.nimi}, joka on {self.lemmikki.kuvaus}"


if __name__ == "__main__":
    hulda = Lemmikki("Hulda", "sekarotuinen koira")
    leevi = Henkilo("Leevi", hulda)
    print(leevi)    # Leevi, kaverina Hulda, joka on sekarotuinen koira

# osa9-07
"""
Class Lahja contains the the name and weight of the gift (kg).
Class Pakkausto adds a parameter to the gift to be given to the package and stores the total weight of the gifts in the package.
"""


class Lahja:
    def __init__(self, nimi: str, paino: int):
        self.nimi = nimi
        self.paino = paino

    def __str__(self):
        return f"{self.nimi} ({self.paino} kg)"


class Pakkaus:
    def __init__(self):
        self.lahja_list = []

    def lisaa_lahja(self, lahja: Lahja):
        self.lahja_list.append(lahja)

    def yhteispaino(self):
        total_weight = 0
        for item in self.lahja_list:
            total_weight = total_weight + item.paino
        return total_weight


if __name__ == "__main__":
    kirja = Lahja("Aapiskukko", 2)
    pakkaus = Pakkaus()
    pakkaus.lisaa_lahja(kirja)
    print(pakkaus.yhteispaino())    # 2
    cd_levy = Lahja("Pink Floyd: Dark side of the moon", 1)
    pakkaus.lisaa_lahja(cd_levy)
    print(pakkaus.yhteispaino())    # 3

# osa9-08
"""
Implement class Huone that contains a list of people with the following methods:
- lisaa(henkilo: Henkilo) add the person given to the parameter in the room.
- on_tyhja() returns the value True or False, which indicates whether the room is empty.
- tulosta_tiedot() prints the people in the room, including the number of people, the total height of people and the info for single person
- lyhin() returns the shortest of the people added to the room
- poista_lyhin() that removes and returns the shortest person from the room
"""


class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi        # Name
        self.pituus = pituus    # Height

    def __str__(self):
        return self.nimi


class Huone:
    def __init__(self):
        self.people_list = []

    def lisaa(self, henkilo: Henkilo):
        self.people_list.append(henkilo)

    def on_tyhja(self):
        if len(self.people_list) == 0:
            return True
        return False

    def tulosta_tiedot(self):
        if not self.on_tyhja():
            total_height = 0
            for item in self.people_list:
                total_height = total_height + item.pituus
            print("Huoneessa {} henkilöä, yhteispituus {} cm".format(
                len(self.people_list), total_height))
            for item in self.people_list:
                print("{} ({} cm)".format(item.nimi, item.pituus))

    def lyhin(self):
        if not self.on_tyhja():
            tmp_dic = {}
            for item in self.people_list:
                tmp_dic[item.nimi] = item.pituus
            for item in self.people_list:
                if item.nimi == min(tmp_dic, key=tmp_dic.get):
                    return item
        return None

    def poista_lyhin(self):
        if self.lyhin() is not None:
            shortest_person = self.lyhin()
            self.people_list.remove(shortest_person)
            return shortest_person
        return None


if __name__ == "__main__":
    huone = Huone()
    print("Huone tyhjä?", huone.on_tyhja())
    print("Lyhin:", huone.poista_lyhin())
    huone.lisaa(Henkilo('Arto', 180))
    huone.lisaa(Henkilo('Jani', 175))
    huone.lisaa(Henkilo('Liisa', 150))
    huone.lisaa(Henkilo('Kimmo', 204))
    huone.lisaa(Henkilo('Jaana', 171))
    huone.lisaa(Henkilo('Aune', 149))
    print()
    print("Lyhin:", huone.poista_lyhin())
    print()
    huone.tulosta_tiedot()

# osa9-09
"""
Implement the following methods for the class Auto:
Two variables for the mileage of driving and the amount of gasoline
- tankkaa(), which fills a gas tank; the contents of the gas tank (0-60 liters)
- aja(km:int), which drives the mileage of the parameter or as far as enough gasoline, the car consumes a liter of petrol per kilometer
- __str__, which shows a description of the car according to the example

Output:
Auto: ajettu 0 km, bensaa 0 litraa
Auto: ajettu 0 km, bensaa 60 litraa
Auto: ajettu 20 km, bensaa 40 litraa
Auto: ajettu 60 km, bensaa 0 litraa
Auto: ajettu 60 km, bensaa 0 litraa
Auto: ajettu 60 km, bensaa 60 litraa
"""


class Auto:
    def __init__(self):
        self.__km = 0
        self.__liter = 0

    def tankkaa(self):
        self.__liter = 60

    def aja(self, km: int):
        if self.__liter >= km:
            self.__km = self.__km + km
            self.__liter = self.__liter - km
        else:
            self.__km = self.__km + self.__liter
            self.__liter = 0

    def __str__(self):
        return "Auto: ajettu {} km, bensaa {} litraa".format(self.__km, self.__liter)


if __name__ == "__main__":
    auto = Auto()
    print(auto)
    auto.tankkaa()
    print(auto)
    auto.aja(20)
    print(auto)
    auto.aja(50)
    print(auto)
    auto.aja(10)
    print(auto)
    auto.tankkaa()
    auto.tankkaa()
    print(auto)

#osa9-10
"""
Implement a class Aanite that models a single recording with one hidden attribute, integer type __pituus
- a constructor that takes length as its parameter
- a detection method pituusthat returns the length
- a setting method that sets the length value
"""
class Aanite:
    def __init__(self, orginal_value: int):
        if orginal_value >= 0:
            self.__pituus = orginal_value
        else:
            raise ValueError("Wrong value")
    
    @property
    def pituus(self):
        return self.__pituus
    
    @pituus.setter
    def pituus(self, new_value: int):
        if new_value >= 0:
            self.__pituus = new_value
        else:
            raise ValueError("Wrong value")

if __name__ == "__main__":
    the_wall = Aanite(-1)
    print(the_wall.pituus)
    the_wall.pituus = 44
    print(the_wall.pituus)
    the_wall.pituus = -1
    print(the_wall.pituus)