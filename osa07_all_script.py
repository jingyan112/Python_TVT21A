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

#osa7-09 tee ratkaisu tänne
"""
Make a program that asks for the user's date of birth (separately day, month, and year) and
prints how many days old the user was on December 31, 1999.
"""
from datetime import datetime

target_time = datetime(1999, 12, 31)
date = int(input("Päivä: "))
month = int(input("Kuukausi: "))
year = int(input("Vuosi: "))
birth_time = datetime(year, month, date)
if target_time > birth_time:
    print(f"Olit {(target_time - birth_time).days} päivää vanha, kun vuosituhat vaihtui.")
else:
    print("Et ollut syntynyt, kun vuosituhat vaihtui.")

#osa7-10 tee ratkaisu tänne
"""
Make a function onko_validi(hetu: str) that returns True or False depending on whether the given ID is correct.
Identity number of the form ppkkvvXyyyz, which ppkkvv tells your date of birth(day/month/year),
X is the birth of a century hanging punctuation mark, yyy a personal and individual number z tarkistemerkki.

The program should check that
    - the beginning is a date in the format ddmmyy, which is an existing date
    - the punctuation mark is +(19th century), -(20th century) or A(2000s) and
    - the check mark at the end is correct.

The check mark is calculated by dividing the series of numbers consisting of
the date of birth and the individual number by 31 and taking the remainder of the division.
The character is then selected from the index of the division remainder from the string 0123456789ABCDEFHJKLMNPRSTUVWXY.
For example, if the remainder is 12, the character in index 12 is selected C.
More information on the calculation can be found, for example, on the website of the Digital and Population Information Agency .
"""
import string

from datetime import datetime

def onko_validi(hetu: str):
    check_mark = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    # Check the length of the SSN
    if len(hetu) != 11:
        return False

    # Check the format of the birth date of the SSN
    for i in range(0, 6):
        if hetu[i] not in string.digits:
            return False
        
    # Check the punctuation mark of the SSN
    if hetu[6] not in ["+", "-", "A"]:
        return False
        
    # Check the validity of the birth date, means check the birth date and the punctuation mark of the SSN
    if hetu[6] == "+":
        year = int("18" + hetu[4] + hetu[5])
    if hetu[6] == "-":
        year = int("19" + hetu[4] + hetu[5])
    if hetu[6] == "A":
        year = int("20" + hetu[4] + hetu[5])
    
    month = int(hetu[2] + hetu[3])
    date = int(hetu[0] + hetu[1])

    isValidDate = True
    try:
        datetime(year, month, date)
    except ValueError:
        isValidDate = False

    if not isValidDate:
        return False
    
    # Check the check mark of the SSN
    if check_mark[int(hetu[0:6] + hetu[7:10]) % 31] != hetu[10]:
        return False
    
    return True 

if __name__ == "__main__":
    print(onko_validi("081842-720N"))

#osa7-11 tee ratkaisu tänne,
"""
The program writes "frame times" to a user-defined file, that is,
the time a user spends on television, a computer, and a mobile device on certain days.

Examples:
yanjing@yanjingdeMacBook-Pro src % python3 ruutuaika.py
Tiedosto: test.txt
Aloituspäivä: 01.09.2020
Montako päivää: 4
Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):
Ruutuaika 01.09.2020:10 10 10
Ruutuaika 02.09.2020:20 20 20
Ruutuaika 03.09.2020:30 30 30
Ruutuaika 04.09.2020:40 40 40
Tiedot tallennettu tiedostoon test.txt

yanjing@yanjingdeMacBook-Pro src % cat test.txt
Ajanjakso: 01.09.2020-04.09.2020
Yht. minuutteja: 300
Keskim. minuutteja: 75.0
01.09.2020: 10/10/10
02.09.2020: 20/20/20
03.09.2020: 30/30/30
04.09.2020: 40/40/40
"""
from datetime import datetime, timedelta

file_name = input("Tiedosto: ")
start_date = input("Aloituspäivä: ")
number_of_days = int(input("Montako päivää: "))

print("Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite): ")

all_time_info = {}
for i in range(0, int(number_of_days)):
    date_time = (datetime.strptime(start_date, "%d.%m.%Y") + timedelta(days=i)).strftime('%d.%m.%Y')
    single_time_info = input(f"Ruutuaika {date_time}:").strip().split(" ")
    all_time_info[date_time] = single_time_info

total_time = 0
for key, value in all_time_info.items():
    tmp = ""
    for i in range(0, len(value)):
        total_time = total_time + int(value[i])
        tmp = tmp + value[i] + "/"
    new_value = tmp[:-1]
    all_time_info[key] = new_value

average_time = total_time / number_of_days

open(file_name, 'w').close()
with open(file_name, 'w') as filename:
    filename.write("Ajanjakso: %s-%s" % (list(all_time_info.keys())[0], list(all_time_info.keys())[-1]) + "\n")
    filename.write("Yht. minuutteja: %s" % total_time + "\n")
    filename.write("Keskim. minuutteja: %s" % average_time + "\n")
    for key, value in all_time_info.items():
        filename.write("%s: %s" % (key, value) + "\n")

print(f"Tiedot tallennettu tiedostoon {file_name}")

#osa7-12 tee ratkaisu tänne
"""
Implement a function tulosta_henkilot(tiedosto: str) that reads an exemplary JSON file with the following format:
    - [{"nimi": "Pekka Pythonisti", "ika": 27, "harrastukset": ["koodaus", "kutominen"]}]
Then prints them in the following format:
    - Pekka Pythonisti 27 vuotta (koodaus, kutominen)
"""
import json

def tulosta_henkilot(tiedosto: str):
    with open(tiedosto) as filename:
        data = filename.read()
    content = json.loads(data)
    for element in content:
        tmp = ""
        for i in element["harrastukset"]:
            tmp = tmp + i + ", "
        sub_element = tmp[:-2]
        print("%s %s vuotta (%s)" % (element["nimi"], element["ika"], sub_element))

if __name__ == "__main__":
    tulosta_henkilot("tiedosto2.json")

#osa7-13 tee ratkaisu tänne
"""
Make a function hae_kaikki() that retrieves and returns data for all running courses (as a field enabledvalue True) in a list of tuple.
The format is as follows: [('Full Stack Open 2020', 'ofs2019', 2020, 201), ('DevOps with Docker 2019', 'docker2019', 2019, 36)]

Make a function in your program hae_kurssi(kurssi: str) that returns more detailed task statistics for the course in a dictionary.
The format is as follows: {'weeks': 4, 'students': 220, 'hours': 5966, 'hours_average': 27, 'tasks': 4988, 'Tasks_average': 22}
"""
import urllib.request as urlrq
import certifi
import json
import ssl

def hae_kaikki():
    courses_information = []
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    res = urlrq.urlopen(url, context=ssl.create_default_context(cafile=certifi.where()))
    # Convert bytes to a string, and then convert string to json
    if type(res.read()) == bytes:
        context = json.loads(res.read().decode("utf-8"))
    else:
        context = json.loads(res.read())
    for item in context:
        if item["enabled"] == True:
            tuple_info = (item["fullName"], item["name"], item["year"], sum(item["exercises"]))
            courses_information.append(tuple_info)
    return courses_information

def hae_kurssi(kurssi: str):
    course_infomation = {}
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses/" + kurssi + "/stats"
    res = urlrq.urlopen(url, context=ssl.create_default_context(cafile=certifi.where()))
    # Convert bytes to a string, and then convert string to json
    if type(res.read()) == bytes:
        context = json.loads(res.read().decode("utf-8"))
    else:
        context = json.loads(res.read())

    weeks_num = 0
    hours_total = 0
    exercise_total = 0
    student_list = []
    for key, value in context.items():
        weeks_num = weeks_num + 1
        student_list.append(value["students"])
        hours_total = hours_total + value["hour_total"]
        exercise_total = exercise_total + value["exercise_total"]
    
    course_infomation["viikkoja"] = weeks_num
    course_infomation["opiskelijoita"] = max(student_list)
    course_infomation["tunteja"] = hours_total
    course_infomation["tunteja_keskimaarin"] = int(hours_total/max(student_list))
    course_infomation["tehtavia"] = exercise_total
    course_infomation["tehtavia_keskimaarin"] = int(exercise_total/max(student_list))

    return course_infomation

#osa7-14 tee ratkaisu tänne
"""
The file tentin_aloitus.csv contains student name and exam start times in the form tunnus;hh:mm.
The file palautus.csv contains student name, tasks, scores and end times in the form tunnus;tehtävä;pisteet;hh:mm.
Write a function huijarit() that returns a list of user IDs for cheated students.
Students whose return on a task has been made more than 3 hours from the start time of the exam will be regarded as cheating.
"""
from datetime import datetime
import csv

def huijarit():
    cheating_list = []
    all_info = []
    with open("tentin_aloitus.csv") as filename1:
        for lines in csv.reader(filename1, delimiter=";"):
            all_info.append({"name": lines[0], "start_time": lines[1], "end_time": 0, "time_cost": 0})

    with open("palautus.csv") as filename2:
        for lines in csv.reader(filename2, delimiter=";"):
            for item in range(0, len(all_info)):
                if all_info[item]["name"] == lines[0]:
                    all_info[item]["end_time"] = lines[3]
                    start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, int(all_info[item]["start_time"].split(":")[0]), int(all_info[item]["start_time"].split(":")[1]))
                    end_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, int(all_info[item]["end_time"].split(":")[0]), int(all_info[item]["end_time"].split(":")[1]))
                    all_info[item]["time_cost"] = float("{:.2f}".format(((end_time - start_time).seconds)/3600))
                    if all_info[item]["time_cost"] > 3:
                        if all_info[item]["name"] not in cheating_list:
                            cheating_list.append(all_info[item]["name"])
    
    return cheating_list

#osa7-15 tee ratkaisu tänne
"""
Write a function viralliset_pisteet() that returns the students' test scores in the dictionary (dict) according to the following rules:
- If multiple returns have been made to the same task number, the return of the highest score will be considered
- If the return is made more than 3 hours after the start of the exam, the return will not be taken into account at all
The tasks are numbered 1–8 and you can get 0–6 points for each task.
In the returned dictionary, the ID is the key and the total score value of the tasks.
This task is based on the previous task.
"""
from datetime import datetime
import csv

def viralliset_pisteet():
    # Deal with the name and start_time csv file
    name_starttime = []
    with open("tentin_aloitus.csv") as filename1:
        for lines in csv.reader(filename1, delimiter=";"):
            name_starttime.append({"name": lines[0], "start_time": lines[1]})

    # Deal with the name, task_id, task_score and end_time csv file
    name_task_time = []
    with open("palautus.csv") as filename2:
        for lines in csv.reader(filename2, delimiter=";"):
            for item in name_starttime:
                if lines[0] == item["name"]:
                    name_task_time.append({"name": lines[0], "task_id": lines[1], "task_score": lines[2], "start_time": item["start_time"], "end_time": lines[3], "time_cost": ""})

    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    
    # Combine the record and calculate the time cost
    for item in name_task_time:
        start_time = datetime(year, month, day, int(item["start_time"].split(":")[0]), int(item["start_time"].split(":")[1]), 0)
        end_time = datetime(year, month, day, int(item["end_time"].split(":")[0]), int(item["end_time"].split(":")[1]), 0)
        item["time_cost"] = float("{:.2f}".format(((end_time - start_time).seconds)/3600))

    # Remove the item with time cost more than 3 hours
    for item in name_task_time:
        if item["time_cost"] > 3:
            name_task_time.remove(item)
    
    for item in name_task_time:
        item.pop("start_time")
        item.pop("end_time")
        item.pop("time_cost")
    
    # Get the record with high task_score for same name and task_id
    tmp = {}
    for item in name_task_time:
        tmp[str(item["name"]) + ":" + str(item["task_id"])] = []
    
    for item in name_task_time:
        tmp[str(item["name"]) + ":" + str(item["task_id"])].append(item["task_score"])

    tmp1 = {}
    final_dic = {}
    for key, value in tmp.items():
        tmp1[key] = max(value)
        final_dic[key.split(":")[0]] = 0

    for key, value in tmp1.items():
        if key.split(":")[0] in final_dic:
            final_dic[key.split(":")[0]] = final_dic[key.split(":")[0]] + int(value)
        
    return final_dic

if __name__ == "__main__":
    viralliset_pisteet()

#osa7-16 tee ratkaisu tänne
"""
As with the version in the previous section, the program prompts the user to enter a line of English text.
The program performs a spell check on the text and prints the same text so that all misspelled words are surrounded by asterisks.
In addition to this, the program provides a list of correction suggestions for misspelled words.

Examples:
write text: We use ptython to make a spell checker

We use * ptython * to make a spell checker
suggestions for improvement:
ptython: python, pythons, Typhon

write text: this is acually a good and usefull program

this is * acually * a good and * usefull * program
suggestions for improvement:
acually: actually, tactually, factually
usefull: usefully, useful, museful
"""
import difflib

sentence_list = input("Write text: ").split(" ")
wrong_words = {}

with open("wordlist.txt") as tiedosto:
    word_dic = []
    for lines in tiedosto:
        lines = lines.replace("\n", "")
        word_dic.append(lines)

for i in range(0, len(sentence_list)):
    if sentence_list[i].lower() not in word_dic:
        wrong_words[sentence_list[i]] = ""
        for item in difflib.get_close_matches(sentence_list[i], word_dic):
            wrong_words[sentence_list[i]] = wrong_words[sentence_list[i]] + item + ", "
        sentence_list[i] = "*" + sentence_list[i] + "*"
    print(sentence_list[i], end = " ")
print()

print("korjausehdotukset:")
for key, value in wrong_words.items():
    print("%s: %s" % (key, value[:-2]))

#osa7-17 tee ratkaisu tänne
"""
Make a module merkkiapuri that includes the following functions:
The function vaihda_koko(merkkijono: str) gets a string as its parameter.
The function creates and returns a new string in which the lowercase letters of the original string are converted to uppercase and vice versa.

The function puolita(merkkijono: str) returns the first and second halves of the string it received as a parameter.
If the string has an odd number of letters, the first half is shorter.

The function poista_erikoismerkit(merkkijono: str) returns a string from which all characters other than the alphabet [a ... ö, A ... Ö], numbers, and spaces have been removed.
"""
import string

def vaihda_koko(merkkijono: str):
    new_string = ""
    for i in merkkijono:
        if i in string.ascii_lowercase:
            new_string = new_string + i.upper()
        elif i in string.ascii_uppercase:
            new_string = new_string + i.lower()
        elif i == "Ö":
            new_string = new_string + "ö"
        elif i == "ö":
            new_string = new_string + "Ö"
        elif i == "Ä":
            new_string = new_string + "ä"
        elif i == "ä":
            new_string = new_string + "Ä"
        elif i == "Å":
            new_string = new_string + "å"
        elif i == "å":
            new_string = new_string + "Å"
        elif i == "Ž":
            new_string = new_string + "ž"
        elif i == "ž":
            new_string = new_string + "Ž"
        else:
            new_string = new_string + i
    return new_string

def puolita(merkkijono: str):
    return merkkijono[0:int(len(merkkijono)/2)], merkkijono[int(len(merkkijono)/2):len(merkkijono)]

def poista_erikoismerkit(merkkijono: str):
    new_string = ""
    for i in merkkijono:
        if i in string.ascii_letters or i in string.digits or i in string.whitespace or i in ["Ö", "ö", "Ä", "ä", "Å", "å", "Ž","ž"]:
            new_string = new_string + i
    return new_string