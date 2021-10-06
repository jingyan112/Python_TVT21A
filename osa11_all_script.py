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