#osa7-01 tee ratkaisu tänne
"""
Make a function hypotenuusa(kateetti1: float, kateetti2: float) that obtains the lengths of the catheters of
a rectangular triangle. The function returns the length of the hypotenuse of a triangle.

Examples:
print(hypotenuusa(3,4)) # 5.0
print(hypotenuusa(5,12)) # 13.0
print(hypotenuusa(1,1)) # 1.4142135623730951
"""
import math
def hypotenuusa(kateetti1: float, kateetti2: float):
    return math.sqrt(kateetti1**2 + kateetti2**2)

if __name__ == "__main__":
    print(hypotenuusa(3,4))
    print(hypotenuusa(5,12))
    print(hypotenuusa(1,1))

#osa7-02 tee ratkaisu tänne
"""
The string module contains string constants that define specific groups of characters (e.g. lowercase letters and punctuation).
Familiarize yourself with these constants and use them to write a function jaa_merkkeihin(merkkijono: str) that gets a string as its parameter.
The function returns a double, in which the characters of the string obtained by the parameter are divided into three different strings:
    - The first string contains all lowercase and uppercase letters in English (standard ascii_letters)
    - The second queue contains all punctuationthe punctuation specified in the standard
    - The third string contains all characters (including, for example, spaces) that do not belong to the previous two groups
    - The characters should be stored in the returned strings in the order in which they appear in the original string.

Expected output:
TmontestiToimiikomit
!!!,?
ää    ä
"""
import string

def jaa_merkkeihin(merkkijono: str):
    first_string = ""
    second_string = ""
    third_string = ""

    try:
        if len(merkkijono) != 0:
            for i in range(0, len(merkkijono)):
                if merkkijono[i] in string.ascii_letters:
                    first_string = first_string + merkkijono[i]
                elif merkkijono[i] in string.punctuation:
                    second_string = second_string + merkkijono[i]
                else:
                    third_string = third_string + merkkijono[i]
    except ValueError:
        pass # invalid string

    return (first_string, second_string, third_string)

if __name__ == "__main__":
    jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")

#osa7-03 tee ratkaisu tänne
"""
Get acquainted with the Python module fractions and use it to implement a function jaa_palasiksi(maara: int) that gets the number of pieces as its parameter. 
The function divides according to the parameter of Chapter 1 into equal fractional pieces and returns these pieces in the list.

Expected output:
1/3
1/3
1/3

[Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5)]
"""
from fractions import Fraction

def jaa_palasiksi(maara: int):
    fraction_list = []
    for i in range(0, maara):
        fraction_list.append(Fraction(1, maara))
    return fraction_list

if __name__ == "__main__":
    for p in jaa_palasiksi(3):
        print(p)
    print()
    print(jaa_palasiksi(5))

#osa7-04 tee ratkaisu tänne
"""
Make a function lottonumerot(maara: int, alaraja: int, ylaraja: int) that
draws a given number of random numbers between alaraja...ylaraja, stores them in a list,
and returns a list. The numbers should be in the returned list in order of magnitude.
Since these are lottery numbers, the same number must not appear twice in the list.
"""
from random import randint

def lottonumerot(maara: int, alaraja: int, ylaraja: int):
    lottery_num = []
    while len(lottery_num) < maara:
        num = randint(alaraja, ylaraja)
        if num not in lottery_num:
            lottery_num.append(num)
    return sorted(lottery_num)

if __name__ == "__main__":
    for numero in lottonumerot(7, 1, 40):
        print(numero, end =" ")
    print()

#osa7-05 tee ratkaisu tänne
"""
Make a function that makes it possible to create passwords of random lengths (between az) of the desired length.

Note:
ASCII table: https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
encode/decode ASCII functions: chr(int); ord(str)
"""
from random import randint

def luo_salasana(length: int):
    password = ""
    while len(password) < length:
        letter = chr(randint(97, 122))
        password = password + letter
    return password

if __name__ == "__main__":
    for i in range(10):
        print(luo_salasana(8))

#osa7-06 tee ratkaisu tänne
"""
Make an improved version of the function in the previous task. 
The function now gets three parameters:
    - if the second parameter is True, the password also contains (one or more) numbers
    - if the third parameter is True, the password also contains (one or more) special characters from the set !?=+-()#
Regardless of the parameters, the password must always contain at least one letter.
You can assume that the function is always called with parameters that make it possible to generate the desired types of passwords.
ASCII: !?=+-()# ==> (33, 63, 61, 43, 45, 40, 41, 35); a-z ==> (97, 122); 0-9 ==> (48, 57)
"""
from random import randint, sample

def luo_hyva_salasana(length: int, boolval1: bool, boolval2: bool):
    password = chr(randint(97, 122))

    special_characters_list = [33, 63, 61, 43, 45, 40, 41, 35]
    if length == 0:
        # Raise error when the length of password is 0
        raise ValueError("Wrong parameters for the function")
    elif length == 1:
        if boolval1 == False and boolval2 == False:
            # The length of password is 1 and should contain 1 letter
            pass
        else:
            # Raise error when the length of password is 1 and should contain at least 1 letter, 1 number and 1 special character
            raise ValueError("Wrong parameters for the function")
    elif length == 2:
        if boolval1 == True and boolval2 == True:
            # Raise error when the length of password is 2 and should contain at least 1 letter, 1 number and 1 special character
            raise ValueError("Wrong parameters for the function")
        elif boolval1 == False and boolval2 == True:
            # The length of password is 2 and should contain 1 letter and 1 special character
            password = password + chr(special_characters_list[randint(0, 7)])
        elif boolval1 == True and boolval2 == False:
            # The length of password is 2 and should contain 1 letter and 1 number
            password = password + chr(randint(48, 57))
        else:
            # The length of password is 2 and should contain 2 letters
            password = password + chr(randint(97, 122))
    else:
        if boolval1 == True and boolval2 == True:
            # Contains at least 1 number, 1 special character and 1 letter
            num_numbers = randint(1, length - 2)
            num_special_characters = randint(1, length - 1 - num_numbers)
            for i in range(0, num_numbers):
                password = password + chr(randint(48, 57))
            for i in range(0, num_special_characters):
                password = password + chr(special_characters_list[randint(0, 7)])
            for i in range(0, length - 1 - num_numbers - num_special_characters):
                password = password + chr(randint(97, 122))  
        elif boolval1 == False and boolval2 == True:
            # Contains at least 1 special character and 1 letter
            num_special_characters = randint(1, length - 1)
            for i in range(0, num_special_characters):
                password = password + chr(special_characters_list[randint(0, 7)])
            for i in range(0, length - 1 - num_special_characters):
                password = password + chr(randint(97, 122))                     
        elif boolval1 == True and boolval2 == False:
            # Contains at least 1 number and 1 letter
            num_numbers = randint(1, length - 1)
            for i in range(0, num_numbers):
                password = password + chr(randint(48, 57))
            for i in range(0, length - 1 - num_numbers):
                password = password + chr(randint(97, 122))
        else:
            # Only contains letter
            for i in range(0, length-1):
                password = password + chr(randint(97, 122))
    
    return ''.join(sample(password, len(password)))

if __name__ == "__main__":
    print(luo_hyva_salasana(1, False, False))
    print(luo_hyva_salasana(2, False, True))
    print(luo_hyva_salasana(2, True, False))
    print(luo_hyva_salasana(2, False, False))
    print(luo_hyva_salasana(10, True, True))
    print(luo_hyva_salasana(10, False, True))
    print(luo_hyva_salasana(10, True, False))
    print(luo_hyva_salasana(10, False, False))

#osa7-07 tee ratkaisu tänne
"""
Make a function heita(noppa: str) that rolls the non-transitive dice multiplied by its parameter.
Dice A has the numbers 3, 3, 3, 3, 3, 6; Dice B have the numbers 2, 2, 2, 5, 5, 5; Dice C have the numbers 1, 4, 4, 4, 4, 4

Make another function pelaa(noppa1: str, noppa2: str, kertaa: int) that throws the number of dice that are parameters as an integer.
The function returns a tuple that tells you the number of times that dice 1 wins, the number of times that dice 2 wins, and the number of times of ties.
"""
from random import randint

def heita(noppa: str):
    dice_dic = {"A": [3, 3, 3, 3, 3, 6], "B": [2, 2, 2, 5, 5, 5], "C": [1, 4, 4, 4, 4, 4]}
    if noppa not in dice_dic:
        raise ValueError("Wrong parameter for this function!")
    return dice_dic[noppa][randint(0,5)]

def pelaa(noppa1: str, noppa2: str, kertaa: int):
    noppa1_noppa2_equal = [0, 0, 0]

    for i in range(0, kertaa):
        noppa1_point = heita(noppa1)
        noppa2_point = heita(noppa2)
        if  noppa1_point > noppa2_point:
            noppa1_noppa2_equal[0] = noppa1_noppa2_equal[0] + 1
        elif noppa1_point < noppa2_point:
            noppa1_noppa2_equal[1] = noppa1_noppa2_equal[1] + 1
        else:
            noppa1_noppa2_equal[2] = noppa1_noppa2_equal[2] + 1

    return (noppa1_noppa2_equal[0], noppa1_noppa2_equal[1], noppa1_noppa2_equal[2])

if __name__ == "__main__":
    tulos = pelaa("A", "B", 1000)
    print(tulos)
    tulos = pelaa("B", "C", 1000)
    print(tulos)
    tulos = pelaa("C", "C", 1000)
    print(tulos)

#osa7-08 tee ratkaisu tänne
"""
The task template contains a file sanat.txt containing English words, one word per line.
Type a function sanat(n: int, alku: str) that returns a list nof random words from a file.
All returned words must begin with the given string.
If the function, for example, were called with parameters sanat(3, "ca"),
it could return the words "cat", "car" and "carbon" in the list, for example.
The same word must not appear twice in the list.
If words beginning with a given string are not found enough to form a group of a given size,
the function produces an exception ValueError.
"""
from random import randint

def sanat(n: int, alku: str):
    word_list = []
    with open("sanat.txt") as filename:
        for lines in filename:
            if lines.replace("\n", "").startswith(alku):
                word_list.append(lines.replace("\n", ""))
    
    random_list = []
    if n > len(word_list):
        raise ValueError("Words beginning with a given string are not found enough to form a group of a given size!")
    else:
        while len(random_list) < n:
            word = word_list[randint(0, len(word_list)-1)]
            if word not in random_list:
                random_list.append(word)
    
    return random_list

if __name__ == "__main__":
    lista = sanat(3, "ca")
    for sana in lista:
        print(sana)