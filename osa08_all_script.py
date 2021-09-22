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

