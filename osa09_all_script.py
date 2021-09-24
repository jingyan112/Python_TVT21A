#osa9-01 Tee ratkaisusi luokan Auto perään
# Älä muuta luokkaa!
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
    return max(new_dic, key = new_dic.get)

# TEE RATKAISUSI TÄHÄN:
if __name__ == "__main__":
    auto1 = Auto("Mersu", 195)
    auto2 = Auto("Lada", 110)
    auto3 = Auto("Ferrari", 280)
    auto4 = Auto("Trabant", 85)

    autot = [auto1, auto2, auto3, auto4]
    print(nopein_auto(autot))

#osa9-02 Tee ratkaisusi luokan Koesuoritus perään.
# ÄLÄ MUUTA LUOKKAA
"""
Write a function hyvaksytyt(suoritukset: list, pisteraja: int) that gets as a parameter a list of test runs and the lowest accepted score as an integer.
The function creates and returns a new list in which only the approved performances from the list are stored.
Do not change the original list or category Koesuoritus.
"""