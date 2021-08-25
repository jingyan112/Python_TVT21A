#osa04-02 tee ratkaisu tänne
"""
Make a function viiva that gets two parameters (width, string).
The function prints a line of the length specified by the first parameter
using the first character of the string in the second parameter. If the string in the parameter is empty,
a dash is printed as asterisks.

Examples:
viiva(7, "%")
viiva(10, "LOL")
viiva(3, "")

%%%%%%% 
LLLLLLLLLL 
***
"""
def viiva(num, string):
    for i in range(0, int(num)):
        if len(string) == 0:
            print("*", end="")
        elif len(string) == 1:
            print(string, end="")
        else:
            print(string[0], end="")
    print("")

if __name__ == "__main__":
    viiva(5, "x")

#osa04-02a tee ratkaisu tänne
"""
Make a function risulaatikko that draws a twig fence mark 
using a twig-box-wide twig box that is the height of its parameter.

Examples:
risulaatikko(5)
print()
risulaatikko(2)

##########
##########
##########
##########
##########

##########
##########
"""
def viiva(num, string):
    for i in range(0, int(num)):
        if len(string) == 0:
            print("*", end="")
        elif len(string) == 1:
            print(string, end="")
        else:
            print(string[0], end="")
    print("")

def risulaatikko(korkeus):
    for i in range(0, int(korkeus)):
        viiva(10, "#")

if __name__ == "__main__":
    risulaatikko(5)

#osa04-02b tee ratkaisu tänne
"""
Make a function risunelio that draws a twig square of its parameter size using a twig fence sign.

Examples:
risunelio(5)
print()
risunelio(3)

##### 
##### 
##### 
##### 
##### 

### 
### 
###
"""
def viiva(num, string):
    for i in range(0, int(num)):
        if len(string) == 0:
            print("*", end="")
        elif len(string) == 1:
            print(string, end="")
        else:
            print(string[0], end="")
    print("")

def risunelio(koko):
    for i in range(0, int(koko)):
        viiva(int(koko), "#")

if __name__ == "__main__":
    risunelio(5)

#osa04-02c tee ratkaisu tänne
"""
Make a function nelio that gets two parameters.
The function prints a square whose height and width are specified by the first parameter.
The second parameter determines which character is used to draw the square.

Examples:
nelio(5, "*")
print()
nelio(3, "o")

***** 
***** 
***** 
***** 
***** 

ooo 
ooo 
ooo
"""
def viiva(num, string):
    for i in range(0, int(num)):
        if len(string) == 0:
            print("*", end="")
        elif len(string) == 1:
            print(string, end="")
        else:
            print(string[0], end="")
    print("")

def nelio(koko, merkki):
    for i in range(0, int(koko)):
        viiva(int(koko), merkki)

if __name__ == "__main__":
    nelio(5, "*")
    print()
    nelio(3, "o")

#osa04-02d tee ratkaisu tänne
"""
Make a function kolmio that draws a twig fence triangle using its parameter height and width.

Examples:
kolmio(6)
print()
kolmio(3)

# 
## 
### 
#### 
##### 
###### 

# 
## 
###
"""
def viiva(num, string):
    for i in range(0, int(num)):
        if len(string) == 0:
            print("*", end="")
        elif len(string) == 1:
            print(string, end="")
        else:
            print(string[0], end="")
    print("")

def kolmio(koko):
    for i in range(1, int(koko)+1):
        viiva(i, "#")

if __name__ == "__main__":
    kolmio(5)

#osa04-03 tee ratkaisu tänne
"""
Make a function kuvio that gets four parameters. 
The function prints a pattern with a triangle defined by the first two parameters at the top
and a rectangle defined by the first and last two parameters at the bottom.

Examples:
kuvio(5, "X", 3, "*")
print()
X 
XX 
XXX 
XXXX 
XXXXX 
***** 
***** 
***** 

kuvio(2, "o", 4, "+")
print()
o 
oo 
++ 
++ 
++ 
++ 

kuvio(3, ".", 0, ",")
print()
. 
.. 
...
"""
def viiva(num, string):
    for i in range(0, int(num)):
        if len(string) == 0:
            print("*", end="")
        elif len(string) == 1:
            print(string, end="")
        else:
            print(string[0], end="")
    print("")

def kuvio(triangle_num, triangle_string, rectangle_num, rectangle_string):
    for i in range(1, int(triangle_num)+1):
        viiva(i, triangle_string)
    for i in range(0, int(rectangle_num)):
        viiva(int(triangle_num), rectangle_string)

if __name__ == "__main__":
    kuvio(5, "x", 2, "o")

#osa04-04 tee ratkaisu tänne
"""
Make a function joulukuusi that gets one parameter.
Function to print the text of the Christmas tree! and a Christmas tree the size of its parameters.

Expected output:
Christmas tree! 
    * 
   *** 
  ***** 
 ******* 
********* 
    *
"""
def joulukuusi(layer):
    print("joulukuusi!")
    for i in range(0, int(layer)):
        dash_num = i * 2 + 1
        blank_num = layer - i - 1
        print(" " * blank_num + "*" * dash_num)
    print(" " * (layer - 1 ) + "*")

if __name__ == "__main__":
    joulukuusi(5)

#osa04-05 tee ratkaisu tänne
"""
Make a function luvuista_suurin that takes three integers as parameters.
The function returns the largest of the numbers using the return statement.
"""
def luvuista_suurin(num1, num2, num3):
    if num1 >= num2:
        tmp = num1
    else:
        tmp = num2

    if tmp >= num3:
        max1 = tmp
    else:
        max1 = num3
    return max1

if __name__ == "__main__":
    suurin = luvuista_suurin(5, 4, 8)
    print(suurin)

#osa04-06 tee ratkaisu tänne
"""
Make a function samat that takes as a parameter a string and two integers representing the indexes of the string.
returnUsing the statement returns , the information ( Trueor False) whether the characters in the positions
indicated by the indexes as parameters of the string are the same. 
If either of the indexes does not match the string, returns the method False.

Example:
# samat merkit o ja o
print(samat("koodari", 1, 2)) # True
"""
def samat(string, num1, num2):
    if num1 < len(string) - 1 and num2 < len(string):
        if string[num1] == string[num2]:
            return True
        else:
            return False
    else:
        return False
if __name__ == "__main__":
    print(samat("koodari", 1, 2))

#osa04-07 tee ratkaisu tänne
"""
Do three functions: eka_sana, toka_sanaand vika_sana.
Each of the functions gets a block (i.e. a string) as its parameter.
Functions, as the name implies, return the first, second, or last word of a sentence.
In each case, you can assume that a string consists of at least two words,
that there is always exactly one space between the words, and that there are no spaces at the beginning and end of the string.

Example:
lause = "olipa kerran kauan sitten ohjelmoija"
print(eka_sana(lause)) # olipa
print(toka_sana(lause)) # kerran
print(vika_sana(lause)) # ohjelmoija
"""
def eka_sana(sentence):
    sentence_list = sentence.split(" ")
    return sentence_list[0]

def toka_sana(sentence):
    sentence_list = sentence.split(" ")
    return sentence_list[1]

def vika_sana(sentence):
    sentence_list = sentence.split(" ")
    return sentence_list[-1]

if __name__ == "__main__":
    lause = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(lause))
    print(toka_sana(lause))
    print(vika_sana(lause))

#osa04-07a Kirjoita ratkaisu tähän
"""
Make a program that initializes a list with values [1, 2, 3, 4, 5].
The program then asks the user for an item index and a new value, changes the value of that item, and reprints the list.
Program execution ends if the user sets the item to index -1.
"""
list_1 = [1, 2, 3, 4, 5]
while True:
    index = int(input("Anna indeksi: "))
    if index == -1:
        break
    else:
        target = int(input("Anna arvo: "))
        list_1[index] = target
        print(list_1)%

#osa04-07b Kirjoita ratkaisu tähän
"""
Make a program that first asks the user for the number of numbers.
The program then asks the user to enter the given number of numbers one by one and adds them to the list in the same order.
"""
numbers = int(input("Kuinka monta lukua: "))
lists = []
for i in range(1, numbers+1):
    lists.append(int(input(f"Anna luku {i}: ")))
print(lists)

#osa04-07c Kirjoita ratkaisu tähän
"""
Make a program that prompts the user to choose to add or remove an item.
Both adding and deleting are done at the end of the list.
The value of the item to be added is always equal to the last item in the list (or 1 if there are no items in the list).

Example:
Lista on nyt []
(l)isää, (p)oista vai e(x)it: l
Lista on nyt [1]
(l)isää, (p)oista vai e(x)it: l
Lista on nyt [1, 2]
(l)isää, (p)oista vai e(x)it: l
Lista on nyt [1, 2, 3]
(l)isää, (p)oista vai e(x)it: p
Lista on nyt [1, 2]
(l)isää, (p)oista vai e(x)it: l
Lista on nyt [1, 2, 3]
(l)isää, (p)oista vai e(x)it: x
Moi!
"""
lista = []
print("Lista on nyt", lista)
while True:
    selection = input("(l)isää, (p)oista vai e(x)it: ")
    if selection == "l":
        lista.append(len(lista)+1)
        print("Lista on nyt", lista)
    if selection == "p":
        lista.pop(-1)
        print("Lista on nyt", lista)
    if selection == "x":
        print("Moi!")
        break

#osa04-08 Kirjoita ratkaisu tähän
"""
Make a program that asks the user for words.
When a user enters a word twice, the program prints the number of different words and stops.
"""
word_list = []
word_list.append(input("sana: "))
while True:
    new_word = input("sana: ")
    if new_word in word_list:
        print(f"Annoit {len(word_list)} eri sanaa")
        break
    else:
        word_list.append(new_word)

#osa04-08b Kirjoita ratkaisu tähän
"""
Make a program that asks the user for numbers and adds them to the list. 
After each chapter is added, the list is printed in two different ways:
- items in the order of insertion and
- arranged from smallest to largest embryo
Program execution ends when the user enters the number 0.
"""
Lista = []
while True:
    num = int(input("Anna luku: "))
    if num == 0:
        print("Moi!")
        break
    else:
        Lista.append(num)
        print("Lista:", Lista)
        print("Järjestettynä:", sorted(Lista))

#osa04-09 tee ratkaisu tänne
"""
Make a function pituusthat returns the length of the list received as a parameter.
"""
def pituus(lista: list):
    return len(lista)

if __name__ == "__main__":
    lista = [3, 6, -4]
    tulos = pituus(lista)
    print(tulos)

#osa04-10 tee ratkaisu tänne
"""
Make a function keskiarvo that returns the average of the items in the integer list that it received as a parameter.
"""
def keskiarvo(lista: list):
    return sum(lista)/len(lista)

if __name__ == "__main__":
    lista = [3, 6, -4]
    tulos = keskiarvo(lista)
    print(tulos)

#osa04-11 tee ratkaisu tänne
"""
Make a function vaihteluvali that returns the range (that is, the difference between the largest and smallest element)
of the list of integers that it receives as a parameter.
"""
def vaihteluvali(lista: list):
    return max(lista) - min(lista)

if __name__ == "__main__":
    lista = [3, 6, -4]
    tulos = vaihteluvali(lista)
    print(tulos)

#osa04-11a Kirjoita ratkaisu tähän
"""
Make a program that asks the user to enter a string and then prints the letters of the string one at a time one below the other.

Example:
Anna merkkijono: Python
P
*
y
*
t
*
h
*
o
*
n
*
"""
text = input("Anna merkkijono: ")
for i in text:
    print(i)
    print("*")

#osa04-11b Kirjoita ratkaisu tähän
"""
Make a program that reads a positive integer N from the user.
The program then prints the numbers between -N ... N except zero.
Each number is printed on its own line.

Example:
Enter the number: 4 
-4 -3 -2 -1 1 2 3 4
"""
positive_num = int(input("Anna luku: "))
negative_num = 0 - positive_num
for i in range(negative_num, positive_num+1):
    if i == 0:
        continue
    else:
        print(i)

#osa04-12 tee ratkaisu tänne
"""
Make a function lista_tahtina that gets a list of integers as a parameter.
The function prints a series of star rows so that the numbers in the list tell you the number of stars in each row.

Example:
lista_tahtina([3, 7, 1, 1, 2])
*** 
******* 
* 
* 
**
"""
def lista_tahtina(lista: list):
    for i in lista:
        for j in range(0, i):
            print("*", end = "")
        print("")

#osa04-13 Tee ratkaisu tänne
"""
Make a function anagrammi that gets two strings as parameters.
The function returns True if the strings are anagrams, that is, they consist of exactly the same letters.

Example:
print(anagrammi("talo", "tola")) # True
print(anagrammi("talo", "lato")) # True
print(anagrammi("talo", "olat")) # True
print(anagrammi("tammi", "mitta")) # False
print(anagrammi("python", "java")) # False
"""
def anagrammi(string1, string2):
    if sorted(string1.lower()) == sorted(string2.lower()):
        return True
    else:
        return False

#osa04-14 tee ratkaisu tänne
"""
Make a function palindromi that gets a string as a parameter and returns True
if the string is a palindrome (that is, with the same content read from beginning to end or end to beginning).

Example:
Anna palindromi: python
ei ollut palindromi
Anna palindromi: java
ei ollut palindromi
Anna palindromi: kauppias
ei ollut palindromi
Anna palindromi: saippuakauppias
saippuakauppias on palindromi!
"""
def palindromi(str1):
    str2 = str1[::-1]
    if str1 == str2:
        return True
    else:
        return False

while True:
    str1 = input("Anna palindromi: ")
    if palindromi(str1):
        print(str1 + " on palindromi!")
        break
    else:
        print("ei ollut palindromi")

#osa04-15 tee ratkaisu tänne
"""
Make a function positiivisten_summa that gets a list of integers as a parameter.
The function returns the sum of the positive numbers in the list.

Expected output:
vastaus 9
"""
def positiivisten_summa(lista):
    sum = 0
    for i in range(0, len(lista)):
        if lista[i] > 0:
            sum = sum + lista[i]
    return sum

if __name__ == "__main__":
    lista = [1, -2, 3, -4, 5]
    vastaus = positiivisten_summa(lista)
    print("vastaus", vastaus)

#osa04-16 tee ratkaisu tänne
"""
Make a function parilliset that gets a list of integers as a parameter.
The function returns a new list with the even numbers contained in the list in the parameter.

Expected output:
alkuperäinen [1, 2, 3, 4, 5]
uusi [2, 4]
"""
def parilliset(lista: list):
    uusi_lista = []
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            uusi_lista.append(lista[i])
    return uusi_lista

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    uusi_lista = parilliset(lista)
    print("alkuperäinen", lista)
    print("uusi", uusi_lista)

#osa04-17 tee ratkaisu tänne
"""
Make a function summa that gets two integer lists as parameters.
Both lists have the same number of items.

Expected output:
[8, 10, 12]
"""
def summa(a: list, b: list):
    sum_list = []
    for i in range(0, len(a)):
        sum_list.append(a[i]+b[i])
    return sum_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b))

#osa04-18 tee ratkaisu tänne
"""
Make a function uniikit that gets a list of integers as a parameter.
The function returns a new list that contains the numbers in the list given
by the parameter in order of magnitude, so that each number is in the list only once.

Expected output:
[1, 2, 3]
"""
def uniikit(lista: list):
    listb = []
    listb.append(lista[0])
    for i in range(1, len(lista)):
        if lista[i] not in listb:
            listb.append(lista[i])
    return sorted(listb)

if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista))

#osa04-18a tee ratkaisu tänne
"""
Make a function pisimman_pituus that gets a list of strings as a parameter.
The function returns the information about the length of the longest string in the list.

Expected output:
9
6
"""
def pisimman_pituus(lista: list):
    listb = []
    for i in range(0, len(lista)):
        listb.append(len(lista[i]))
    return sorted(listb)[-1]

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]
    tulos = pisimman_pituus(lista)
    print(tulos)
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
    tulos = pisimman_pituus(lista)
    print(tulos)

#osa04-18b tee ratkaisu tänne
"""
Make a function lyhin that gets a list of strings as a parameter.
The function prints the shortest string in the list.
If there are several of the same length (this is not the case in tests), the function can return any of them.
The function can assume that there are no empty, that is, zero-length strings in the list.

Expected output:
eka
eero
"""
def lyhin(lista: list):
    dica = {}
    for i in range(0, len(lista)):
        dica[lista[i]] = len(lista[i])
    return min(dica, key=dica.get)

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]
    tulos = lyhin(lista)
    print(tulos)
    lista = ["pekka", "emilia", "johanna", "venla", "eero", "antti"]
    tulos = lyhin(lista)
    print(tulos)

#osa04-19 tee ratkaisu tänne
"""
Make a function pisimmat that gets a list of strings as a parameter.
The function returns a list that contains the longest string in the list given by the parameter.
If there are more than one longest string, the function returns all of them in the list.

Expected output:
['seitsemäs']
['emilia', 'juhani']
"""
def pisimmat(lista: list):
    res_list = []
    dica = {}
    for i in range(0, len(lista)):
        dica[lista[i]] = len(lista[i])
    for index, value in dica.items():
        if value == dica[max(dica, key=dica.get)]:
            res_list.append(index)
    return res_list

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]

    tulos = pisimmat(lista)
    print(tulos) 

    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
    tulos = pisimmat(lista)
    print(tulos)

#osa04-20 tee ratkaisu tänne
"""
Write a function muotoile that gets a list of floating-point numbers as its parameter.
Based on the list, the function generates a new list of strings,
in which each item in the floating-point list is shown rounded to two decimal places.
The order of the items in the list must be maintained.

Expected output:
['1.23', '0.33', '0.11', '3.45']
"""
def muotoile(lista: list):
    new_lista = []
    for i in range(0, len(lista)):
        new_lista.append(str(f'{lista[i]:.2f}'))
    return new_lista

if __name__ == "__main__":
    lista = [1.234, 0.3333, 0.11111, 3.446]
    lista2 = muotoile(lista)
    print(lista2)

#osa04-21 tee ratkaisu tänne
"""
Write a function kaikki_vaarinpain that gets a list of strings as its parameter.
The function creates and returns a new list in which all strings in the original list are translated.
The order of the items in the list is also reversed.

Expected output:
['isky äleiv', 'ikkremise', 'ikkiak', 'ioM']
"""
def kaikki_vaarinpain(lista: list):
    new_lista = []
    for i in range(len(lista)-1, -1, -1):
        single_element = lista[i]
        new_lista.append(single_element[len(single_element)::-1])
    return new_lista

if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)

#osa04-22 tee ratkaisu tänne
"""
Write a function eniten_kirjainta that gets a string as its parameter.
The function returns the letter that appears most in the string.
If there are many equally common letters, the function must return the first one in the string.

Expected output:
b
k
"""
def eniten_kirjainta(stringa: str):
    new_lista = []
    new_lista.append(stringa[0])
    for i in range(1,len(stringa)):
        if stringa[i] not in new_lista:
            new_lista.append(stringa[i])

    dic_lista = {}
    for i in range(0, len(new_lista)):
        dic_lista[new_lista[i]] = stringa.count(new_lista[i])

    return max(dic_lista, key=dic_lista.get)

if __name__ == "__main__":
    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono))

    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))

#osa04-23 tee ratkaisu tänne
"""
Write a function ilman_vokaaleja that gets a string as its parameter.
The function returns a new string with the vowels of the original string removed.
You can assume that the string consists only of lowercase Finnish letters a ... ö.

Expected output:
tm n smrkk
"""
def ilman_vokaaleja(stringa: str):
    new_stringa = ""
    for i in range(0, len(stringa)):
        if stringa[i] not in ['ä', 'a', 'å', 'e', 'i', 'o', 'ö', 'u', 'y']:
            new_stringa = new_stringa + stringa[i]
    return new_stringa

if __name__ == "__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))

#osa04-24 tee ratkaisu tänne
"""
Write a function poista_isot that gets a list of strings as its parameter.
The function returns a new list with the strings that do not consist of all uppercase letters from the list in its parameter.

Expected output:
['def', 'pieni', 'toinen pieni', 'Osittain Iso']
"""
def poista_isot(lista: list):
    new_lista = []
    for i in range(0, len(lista)):
        if not lista[i].isupper():
            new_lista.append(lista[i])
    return new_lista

if __name__ == "__main__":
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)

#osa04-25 tee ratkaisu tänne
"""
Write a function pisin_naapurijono that finds the longest sublist of consecutive neighbors in the list and returns its length.
For example, the [1, 2, 5, 4, 3, 4]longest such sub-list in the list would be [5, 4, 3, 4], and its length 4.

Expected output:
6
"""
def pisin_naapurijono(lista: list):
    alllist_dic = {}

    for i in range(0, len(lista)):
        alllist_dic[i] = [lista[i]]
        for j in range(i, len(lista)-1):
            if (lista[j] - lista[j+1] == 1 or lista[j] - lista[j+1] == -1):
                alllist_dic[i].append(lista[j+1])
            else:
                break

    new_dic = {}
    for key, value in alllist_dic.items():
        new_dic[key] = len(value)
    print(new_dic)

    return new_dic[max(new_dic, key=new_dic.get)]

if __name__ == "__main__":
    lista = [1, 2, 3, 0, 1, 2, 3, 4, 5, 3, 4, 5, 1, 2, 3]
    print(pisin_naapurijono(lista))

#osa04-26 tee ratkaisu tänne
"""
In this task, a program for printing course grade statistics is implemented.
Lines are entered into the program that contain the number of test points per student and the number of assignments completed.
Based on them, the program prints statistics related to grades.
Test scores are integers between 0 and 20. 
The numbers of the completed exercises, on the other hand, are integers between 0 and 100.
The program queries the user for lines until the user enters an empty line.
You can assume that all rows are entered "correctly," that is, a row has either two integers or a row is blank.

Once the user has entered a blank line, the program prints statistics.
The statistics are as follows:
Assignments made in the receiver of the number of exercise points such that
at least 10% of the amount will be one training point, 20% exercise brings two points, etc., and 100%, or 100 exercises related to that of 10 training points.
The score obtained from the exercises is an integer.

The grade of the course is determined by the sum of the exam points and the points obtained from the assignments according to the following table:
test points + practice points	grade
0-14	0 (i.e. rejected)
15–17	1
18-20	2
21–23	3
24–27	4
28–30	5

However, there is an exception to the above:
if the test score is less than 10, the grade is 0, regardless of the total score, ie rejected.

Examples:
Koepisteet ja harjoitusten määrä: 15 87
Koepisteet ja harjoitusten määrä: 10 55
Koepisteet ja harjoitusten määrä: 11 40
Koepisteet ja harjoitusten määrä: 4 17
Koepisteet ja harjoitusten määrä:

Tilasto:
Pisteiden keskiarvo: 14.5
Hyväksymisprosentti: 75.0
Arvosanajakauma:
  5:
  4:
  3: *
  2:
  1: **
  0: *
"""
test_list = []
exercise_list = []
while True:
    input_data = input("Koepisteet ja harjoitusten määrä: ")
    if input_data == "":
        break    
    else:
        test_list.append(int(input_data.split(" ")[0]))
        exercise_list.append(int(int(input_data.split(" ")[1]) / 10))

print("Tilasto:")
score_list = []
reject_num = 0
score_sum = 0

for i in range(0, len(test_list)):
    score_sum = score_sum + test_list[i] + exercise_list[i]
    if test_list[i] < 10:
        score_list.append(0)
        reject_num = reject_num + 1
    else:
        score_list.append(test_list[i] + exercise_list[i])
        
score_avg = score_sum / len(test_list)
print("Pisteiden keskiarvo:", score_avg)

rate_dic = {'5': 0, '4': 0, '3':0, '2': 0, '1': 0, '0': 0}

for i in range(0, len(score_list)):
    if score_list[i] >= 0 and score_list[i] <= 14:
        rate_dic['0'] = rate_dic['0'] + 1
    elif score_list[i] >= 15 and score_list[i] <= 17:
        rate_dic['1'] = rate_dic['1'] + 1
    elif score_list[i] >= 18 and score_list[i] <= 20:
        rate_dic['2'] = rate_dic['2'] + 1
    elif score_list[i] >= 21 and score_list[i] <= 23:
        rate_dic['3'] = rate_dic['3'] + 1
    elif score_list[i] >= 24 and score_list[i] <= 27:
        rate_dic['4'] = rate_dic['4'] + 1
    else:
        rate_dic['5'] = rate_dic['5'] + 1

reject_rate = 100 - rate_dic['0'] * 100 / len(test_list)
print("Hyväksymisprosentti:", f'{reject_rate:.1f}')

print("Arvosanajakauma:")
for key, value in rate_dic.items():
    print("  " + key + ": ", end = "")
    for i in range(0, value):
        print("*", end = "")
    print()