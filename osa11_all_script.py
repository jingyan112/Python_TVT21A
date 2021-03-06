#osa11-1
"""
Using a list compilation to implement neliojuuret(luvut: list)
gets a list of integers as a parameter
returns a list of the square roots of the numbers in the parameter.

Output:
1.0
1.4142135623730951
1.7320508075688772
2.0
"""
import math
def neliojuuret(luvut: list):
    return [math.sqrt(element) for element in luvut]

if __name__ == "__main__":
    rivit = neliojuuret([1,2,3,4])
    for rivi in rivit:
        print(rivi)

#osa11-2
"""
Using a list compilation to implement tahtirivit(luvut: list)
 gets a list of integers as a parameter
returns a list consisting of rows of stars whose length corresponds to the numbers in the list in the parameter.

Output:
*
**
***
****

****
***
**
*
**********
"""
def tahtirivit(luvut: list):
    return ["*"*element for element in luvut]

if __name__ == "__main__":
    rivit = tahtirivit([1,2,3,4])
    for rivi in rivit:
        print(rivi)

    print()

    rivit = tahtirivit([4, 3, 2, 1, 10])
    for rivi in rivit:
        print(rivi)

#osa11-3
"""
Using a list compilation to implement parhaat_tulokset(suoritukset: list)
gets a list of test execution objects as its parameter.
returns a new list that stores the best rating for each run.

Output:
[5, 4, 3]
"""
# class Koesuoritus: name, rating1, rating2, rating3
class Koesuoritus:
    def __init__(self, nimi: str, arvosana1: int, arvosana2: int, arvosana3: int):
        self.nimi = nimi
        self.arvosana1 = arvosana1
        self.arvosana2 = arvosana2
        self.arvosana3 = arvosana3

    def __str__(self):
        return (f'Nimi:{self.nimi}, arvosana1: {self.arvosana1}' +
            f', arvosana2: {self.arvosana2}, arvosana3: {self.arvosana3}')

def parhaat_tulokset(suoritukset: list):
    return [max([element.arvosana1, element.arvosana2, element.arvosana3]) for element in suoritukset]

if __name__ == "__main__":
    suoritus1 = Koesuoritus("Pekka",5,3,4)
    suoritus2 = Koesuoritus("Pirjo",3,4,1)
    suoritus3 = Koesuoritus("Paavo",2,1,3)
    suoritukset = [suoritus1, suoritus2, suoritus3]
    print(parhaat_tulokset(suoritukset))

#osa11-4
"""
Using a list compilation to implement pituudet(listat: list)
gets a list containing lists that contain integers
returns a list containing the lengths of the lists in the parameter.

Output:
[5, 4, 0]
"""
def pituudet(listat: list):
    return [len(element) for element in listat]

if __name__ == "__main__":
    listat = [[1,2,3,4,5], [324, -1, 31, 7],[]]
    print(pituudet(listat))

#osa11-5
"""
Using a list compilation with a conditional part to implement poista_pienemmat(luvut: list, raja: int)
gets a list of integers and a limit value that is also an integer
returns a new list with numbers below the limit value omitted.

Output:
[65, 32, 11]
[7, 8]
"""
def poista_pienemmat(luvut: list, raja: int):
    return [element for element in luvut if element >= raja]

if __name__ == "__main__":
    lukuja = [1,65, 32, -6, 9, 11]
    print(poista_pienemmat(lukuja, 10))
    print(poista_pienemmat([-4, 7, 8, -100], 0))

#osa11-6
"""
Using a list compilation with a conditional part to implement vokaalilla_alkavat(sanat: list)
gets a list of strings as its parameter
returns a new list that contains only those words from the original list that begin with a vowel (a, e, i, o, u, y, ??, ??)
Both uppercase and lowercase letters must be valid.
"""
def vokaalilla_alkavat(sanat: list):
    return [element for element in sanat if element[0].lower() in ["a", "e", "i", "o", "u", "y", "??", "??"]]

if __name__ == "__main__":
    klista = ["auto","mopo","Etana","kissa","Koira","OMENA","appelsiini"]
    for vok in vokaalilla_alkavat(klista):
        print(vok)

#osa11-7
"""
Implement a class Lottorivi
- the constructor gets a round number (integer) and a seven-item integer list
- osumien_maara(pelattu_rivi: list) method returns times of hits of the element in pelattu_rivi to the seven-item integer list
- osumat_paikoillaan(pelattu_rivi: list) method returns a new list has the hitting numbers in their old places and others are replaced by -1 
"""
class Lottorivi:
    def __init__(self, round_num: int, seven_item: list):
        self.round_num = round_num
        self.seven_item = seven_item
    
    def osumien_maara(self, pelattu_rivi: list):
        return len([element for element in pelattu_rivi if element in self.seven_item])
    
    def osumat_paikoillaan(self, pelattu_rivi: list):
        return [element if element in self.seven_item else -1 for element in pelattu_rivi]

if __name__ == "__main__":
    oikea = Lottorivi(5, [1,2,3,4,5,6,7])
    oma_rivi = [1,4,7,11,13,19,24]
    print(oikea.osumien_maara(oma_rivi))    # 3

    oikea = Lottorivi(8, [1,2,3,10,20,30,33])
    oma_rivi = [1,4,7,10,11,20,30]
    print(oikea.osumat_paikoillaan(oma_rivi))   # [1, -1, -1, 10, -1, 20, 30]

#osa11-8
"""
Using a list compilation with a conditional part to implement suodata_kielletyt(merkkijono: str, kielletyt: str)
returns a newstring in its parameter that does not contain any characters from its second parameter.

Output:
Suo kuokka ja python hieno yhdistelm??
"""
def suodata_kielletyt(merkkijono: str, kielletyt: str):
    return "".join([element for element in list(merkkijono) if element not in list(kielletyt)])

if __name__ == "__main__":
    lause = "Suo! kuokka, ja python: hieno yhdistelm??!??!?!"
    suodatettu = suodata_kielletyt(lause, "!?:,.")
    print(suodatettu)

#osa11-9
"""
Using a list compilation with a conditional part to implement kauppalistan_tuotteet(kauppalista: list, maara: int)
gets a trade list object as a parameter
returns the names of the products with maara attribute not less than the second parameter.

Output:
kauppalistalla v??hint????n 8 seuraavia tuotteita:
banaanit
alkoholiton olut
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
        if self.n < len(self.tuotteet):
            tuote = self.tuotteet[self.n]
            self.n += 1
            return tuote
        else:
            raise StopIteration

def kauppalistan_tuotteet(kauppalista: list, maara: int):
    return [item[0] for item in kauppalista if item[1] >= maara]

if __name__ == "__main__":
    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("alkoholiton olut", 24)
    lista.lisaa("ananas", 1)

    print("kauppalistalla v??hint????n 8 seuraavia tuotteita:")
    for tuote in kauppalistan_tuotteet(lista, 8):
        print(tuote)
    
#osa11-10
"""
Using a list compilation with a conditional part to implement kauppalistan_tuotteet(kauppalista: list, maara: int)
gets a list of dwellings and an individual dwelling to be compared
returns a list of the apartments that are cheaper than the comparable apartment, and the price difference between them

Output:
asuntoa Jakom??ki kolmio halvemmat vaihtoehdot:
Eira yksi??                     hintaero 107000 euroa
Kallio kaksio                  hintaero 35400 euroa
Suomussalmi omakotitalo        hintaero 87500 euroa
Kerava 4h ja keitti??           hintaero 16500 euroa
"""
class Asunto:
    def __init__(self, huoneita: int, nelioita: int, neliohinta:int, kuvaus: str):
        self.huoneita = huoneita
        self.nelioita = nelioita
        self.neliohinta = neliohinta
        self.kuvaus = kuvaus

    def suurempi(self, verrattava):
        return self.nelioita > verrattava.nelioita

    def hintaero(self, verrattava):
        ero = abs((self.neliohinta * self.nelioita) - (verrattava.neliohinta * verrattava.nelioita))
        return ero

    def kalliimpi(self, verrattava):
        ero = (self.neliohinta * self.nelioita) - (verrattava.neliohinta * verrattava.nelioita)
        return ero > 0

    def __repr__(self):
        return (f'Asunto(huoneita = {self.huoneita}, nelioita = {self.nelioita}, ' + 
            f'neliohinta = {self.neliohinta}, kuvaus = {self.kuvaus})')

def halvemmat(asunnot: list, verrattava: Asunto):
    return [(item, item.hintaero(verrattava)) for item in asunnot if not item.kalliimpi(verrattava) and item != verrattava]

if __name__ == "__main__":
    a1 = Asunto(1, 16, 5500, "Eira yksi??")
    a2 = Asunto(2, 38, 4200, "Kallio kaksio")
    a3 = Asunto(3, 78, 2500, "Jakom??ki kolmio")
    a4 = Asunto(6, 215, 500, "Suomussalmi omakotitalo")
    a5 = Asunto(4, 105, 1700, "Kerava 4h ja keitti??")
    a6 = Asunto(25, 1200, 2500, "Haikon kartano")

    asunnot = [a1, a2, a3, a4, a5, a6]

    print(f"asuntoa {a3.kuvaus} halvemmat vaihtoehdot:")
    for alkio in halvemmat(asunnot, a3):
        print(f"{alkio[0].kuvaus:30} hintaero {alkio[1]} euroa")

#osa11-11
"""
Using a dictionary compilation with a conditional part to implement pituudet(merkkijonot: list)
gets a list of strings as a parameter
returns a dictionary with keys as list strings and values ??????as string lengths.

Output:
{'suo': 3, 'kuokka': 6, 'python': 6, 'ja': 2, 'koodari': 7}
"""
def pituudet(merkkijonot: list):
    return {item: len(item) for item in merkkijonot}

if __name__ == "__main__":
    sanalista = ["suo", "kuokka" , "python", "ja", "koodari"]
    sanojen_pituudet = pituudet(sanalista)
    print(sanojen_pituudet)

#osa11-12
"""
Using a dictionary compilation with a conditional part to implement yleisimmat_sanat(tiedoston_nimi: str, raja: int)
gets the file name as its parameter
returns a dictionary that contains the number of occurrences of the words not less than raja
Note: The punctuation should be removed first, otherwise, they will influence the count()
"""
import string
def yleisimmat_sanat(tiedoston_nimi: str, raja: int):
    all_info = ""
    with open(tiedoston_nimi) as file_name:
        for line in file_name:
            all_info += line.replace("\n", " ")
    all_info = "".join([element for element in list(all_info) if element not in string.punctuation])
    word_list = all_info.split(" ")
    return {word: word_list.count(word) for word in word_list if word_list.count(word) >= raja}

if __name__ == "__main__":
    print(yleisimmat_sanat("comprehensions.txt", 4))        # {'comprehension': 4, 'list': 4}

#osa10-13
"""
Write a recursive function listaan_lukuja(luvut: list) that adds numbers to the list
until the length of the list is divisible by five.
Each number added to the list is always one greater than the last number in the list.

Output:
[1, 3, 4, 5, 10, 11, 12, 13, 14, 15]
"""
def listaan_lukuja(luvut: list):
    if len(luvut)%5 != 0:
        luvut.append(luvut[-1]+1)
        listaan_lukuja(luvut)

if __name__ == "__main__":
    luvut = [1,3,4,5,10,11]
    listaan_lukuja(luvut)
    print(luvut)

#osa10-14
"""
Write a recursive function def summa(luku: int) that calculate the summa(luku: int)sum 1 + 2 + ... + luku.

Output:
6
15
55
"""
def summa(luku: int):
    if luku <= 1:
        return luku
    return luku + summa(luku-1)

if __name__ == "__main__":
    tulos = summa(3)
    print(tulos)
    print(summa(5))
    print(summa(10))

#osa11-15
"""
Using recursion algrithorim to implement sulut_tasapainossa(merkkijono: str)
which checks whether the each "opening" parenthesis/square bracket in the string has its own "closing" parenthesis/square bracket.
return True if so, otherwise, return False
"""
def sulut_tasapainossa(merkkijono: str):
    merkkijono = "".join(element for element in list(merkkijono) if element in ["(", "[", ")", "]"])
    if len(merkkijono) == 0:
        return True
    if (merkkijono[0] == '(' and merkkijono[-1] != ')') or (merkkijono[0] == '[' and merkkijono[-1] != ']') or merkkijono[0] == ')' or merkkijono[0] == ']':
        return False
    return sulut_tasapainossa(merkkijono[1:-1])

if __name__ == "__main__":
    print(sulut_tasapainossa("(((())))"))                           # True
    print(sulut_tasapainossa("()())"))                              # False
    print(sulut_tasapainossa(")()"))                                # False
    print(sulut_tasapainossa("()(())"))                             # False
    print(sulut_tasapainossa("([([])])"))                           # True
    print(sulut_tasapainossa("(python versio [3.7]) k??yt?? t??t??!"))  # True
    print(sulut_tasapainossa("(()]"))                               # False
    print(sulut_tasapainossa("([huono)]"))                          # False
    print(sulut_tasapainossa("(x)y)"))                              # False

#osa11-16
"""
Traverse the binary tree and find the node with the largest value

Output:
original target:  2
original target:  3
original target:  15
after target:  15
original target:  15
after target:  15
target, juuri.arvo, suurin_alkio(juuri.vasen_lapsi) (15, 3, 15)
original target:  48
after target:  48
original target:  48
after target:  48
target, juuri.arvo, suurin_alkio(juuri.oikea_lapsi) (48, 3, 48)
after target:  48
original target:  3
original target:  15
after target:  15
original target:  15
after target:  15
target, juuri.arvo, suurin_alkio(juuri.vasen_lapsi) (15, 3, 15)
original target:  48
after target:  48
original target:  48
after target:  48
target, juuri.arvo, suurin_alkio(juuri.oikea_lapsi) (48, 3, 48)
after target:  48
target, juuri.arvo, suurin_alkio(juuri.vasen_lapsi) (48, 2, 48)
original target:  4
original target:  11
after target:  11
original target:  11
after target:  11
target, juuri.arvo, suurin_alkio(juuri.oikea_lapsi) (11, 4, 11)
after target:  11
original target:  4
original target:  11
after target:  11
original target:  11
after target:  11
target, juuri.arvo, suurin_alkio(juuri.oikea_lapsi) (11, 4, 11)
after target:  11
target, juuri.arvo, suurin_alkio(juuri.oikea_lapsi) (48, 2, 11)
after target:  48
48
"""
# class Alkio, describing a binary tree
class Alkio:
    def __init__(self, arvo, vasen_lapsi:'Alkio' = None, oikea_lapsi:'Alkio' = None):
        self.arvo = arvo                # root node
        self.vasen_lapsi = vasen_lapsi  # left node
        self.oikea_lapsi = oikea_lapsi  # right node

def suurin_alkio(juuri: Alkio):
    target = juuri.arvo
    #print("original target: ", target)

    if juuri.vasen_lapsi is not None:
        target = max(target, juuri.arvo, suurin_alkio(juuri.vasen_lapsi))
        #print("target, juuri.arvo, suurin_alkio(juuri.vasen_lapsi)", (target, juuri.arvo, suurin_alkio(juuri.vasen_lapsi)))

    if juuri.oikea_lapsi is not None:
        target = max(target, juuri.arvo, suurin_alkio(juuri.oikea_lapsi))
        #print("target, juuri.arvo, suurin_alkio(juuri.oikea_lapsi)", (target, juuri.arvo, suurin_alkio(juuri.oikea_lapsi)))
    
    #print("after target: ", target)

    return target

if __name__ == "__main__":
    puu = Alkio(2)
    puu.vasen_lapsi = Alkio(3)
    puu.vasen_lapsi.vasen_lapsi = Alkio(15)
    puu.vasen_lapsi.oikea_lapsi = Alkio(48)
    puu.oikea_lapsi = Alkio(4)
    puu.oikea_lapsi.oikea_lapsi = Alkio(11)
    print(suurin_alkio(puu))    # 48

#osa11-17
"""
Make a function laske_alaiset(tyontekija: Tyontekija) that recursively 
calculates the number of subordinates of a given employee.
"""
# class Tyontekija, describe the employee name and his/her subordinates
class Tyontekija:
    def __init__(self, nimi: str):
        self.nimi = nimi
        self.alaiset = []

    def lisaa_alainen(self, tyontekija: 'Tyontekija'):
        self.alaiset.append(tyontekija)

def laske_alaiset(tyontekija: Tyontekija):
    subordinates = len(tyontekija.alaiset)
    for element in tyontekija.alaiset:
        subordinates += laske_alaiset(element)
    return subordinates

if __name__ == "__main__":
    t1 = Tyontekija("Sasu")
    t2 = Tyontekija("Erkki")
    t3 = Tyontekija("Matti")
    t4 = Tyontekija("Emilia")
    t5 = Tyontekija("Antti")
    t6 = Tyontekija("Kjell")
    t1.lisaa_alainen(t4)
    t1.lisaa_alainen(t6)
    t4.lisaa_alainen(t2)
    t4.lisaa_alainen(t3)
    t4.lisaa_alainen(t5)
    print(laske_alaiset(t1))
    print(laske_alaiset(t4))
    print(laske_alaiset(t5))

#osa11-18
"""
Implement a class Tehtava (task):
- with attributes: id, description, software comapny name, estimation of workload, complete_status
  - the id starts from 1 (the first task to be created gets an id of 1, the next an id of 2, etc)
  - the complete_status of the task is False at the time it is created
- the complete_status of the task can be checked with trhe method on_valmis(self)
- the complete_status of the task can be marked by calling the method merkkaa_valmiiksi(self)

Implement a class Tilauskirja which compiles all the Tehtava objects:
- lisaa_tilaus(self, kuvaus, koodari, tyomaara) method add a new order to the order book
- kaikki_tilaukset(self) method returns all tasks
- koodarit(self) method returns as a list all software comapny names in the tasks without repeating
- merkkaa_valmiiksi(self, id: int) marks the task with id as completed, if no matching, raise ValueError
- valmiit_tilaukset(self) method returns a list of complete tasks
- ei_valmiit_tilaukset(self) method returns a list of unfinished tasks
- koodarin_status(self, koodari: str) method returns a tuple of tasks with koodari, if no matching, raise ValueError
  (complete_tasks, unfinished_tasks, complete_tasks_workload, unfinished_tasks_workload)
"""
class id_generator:
    def __init__(self):
        self.count = 0
    
    def id_caller(self):
        self.count += 1
        return self.count

# kuvaus(description), koodari(software comapny name), tyomaara(estimation of workload)
class Tehtava:
    global id_counting
    id_counting = id_generator()

    def __init__(self, kuvaus: str, koodari: str, tyomaara: int, complete_status: bool = False):
        self.id = id_counting.id_caller()
        self.kuvaus = kuvaus
        self.koodari = koodari
        self.tyomaara = tyomaara
        self.complete_status = complete_status
    
    def on_valmis(self):
        return self.complete_status
    
    def merkkaa_valmiiksi(self):
        self.complete_status = True

    def __str__(self):
        if self.on_valmis():
            return "{}: {} ({} tuntia), koodari {} VALMIS".format(self.id, self.kuvaus, self.tyomaara, self.koodari)   
        else:
            return "{}: {} ({} tuntia), koodari {} EI VALMIS".format(self.id, self.kuvaus, self.tyomaara, self.koodari)

class Tilauskirja:
    def __init__(self):
        self.task_list = []

    def lisaa_tilaus(self, kuvaus: str, koodari: str, tyomaara: int):
        self.task_list.append(Tehtava(kuvaus, koodari, tyomaara))
    
    def kaikki_tilaukset(self):
        return self.task_list
    
    def koodarit(self):
        return list(set([element.koodari for element in self.task_list]))

    def merkkaa_valmiiksi(self, id: int):
        matching_times = 0
        for element in self.task_list:
            if id == element.id:
                element.merkkaa_valmiiksi()
                matching_times += 1
        if matching_times == 0:
            raise ValueError("No matching")
    
    def valmiit_tilaukset(self):
        return [element for element in self.task_list if element.on_valmis()]
    
    def ei_valmiit_tilaukset(self):
        return [element for element in self.task_list if not element.on_valmis()]
    
    def koodarin_status(self, koodari: str):
        matching_times = 0
        completed_tasks = 0
        completed_tasks_workload = 0
        unfinished_tasks = 0
        unfinished_tasks_workload =0

        for element in self.task_list:
            if element.koodari == koodari:
                matching_times += 1
                if element.on_valmis():
                    completed_tasks += 1
                    completed_tasks_workload += element.tyomaara
                else:
                    unfinished_tasks += 1
                    unfinished_tasks_workload += element.tyomaara
        
        if matching_times == 0:
            raise ValueError("No matching")
        else:
            return (completed_tasks, unfinished_tasks, completed_tasks_workload, unfinished_tasks_workload)