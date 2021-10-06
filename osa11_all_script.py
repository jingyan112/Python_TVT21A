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
returns a new list that contains only those words from the original list that begin with a vowel (a, e, i, o, u, y, ä, ö)
Both uppercase and lowercase letters must be valid.
"""
def vokaalilla_alkavat(sanat: list):
    return [element for element in sanat if element[0].lower() in ["a", "e", "i", "o", "u", "y", "ä", "ö"]]

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