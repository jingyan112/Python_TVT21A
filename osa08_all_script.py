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