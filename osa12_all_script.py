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