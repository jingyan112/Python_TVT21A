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