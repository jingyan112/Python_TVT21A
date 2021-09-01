#osa6-01 tee ratkaisu tänne
"""
The file luvut.txtis stored numbers, one number per line.
Type a function suurin that reads the file and returns the largest number found in the file.
"""
def suurin():
    num_list = []
    with open("luvut.txt") as tiedosto:
        for num in tiedosto:
            num_list.append(int(num))
    return max(num_list)

#osa6-02 tee ratkaisu tänne
"""
The file hedelmat.csv contains fruit with prices.
Write a function lue_hedelmat that reads the fruit file and forms a dictionary from it,
where the fruit name is the key and the price value. The price must be in the float dictionary.
Finally, the function returns this dictionary.
"""
def lue_hedelmat():
    fruit_dic = {}
    with open("hedelmat.csv") as tiedosto:
        for line in tiedosto:
            line = line.replace("\n", "")
            fruit_info = line.split(";")
            fruit_dic[fruit_info[0]] = float(fruit_info[1])
    return fruit_dic

#osa6-03 tee ratkaisu tänne
"""
The file matriisi.txt has a matrix.
Write the functions summa and maksimi that read and return, as their name implies,
the sum and largest element of all the elements in the matrix.
In addition, write a function rivisummat that returns the sums
of all the rows in the matrix in the list.
"""
def summa():
    number_list = []
    with open("matriisi.txt") as tiedosto:
        for line in tiedosto:
            line = line.replace("\n", ",")
            all_numbers = line.split(",")
            for i in all_numbers:
                if i != '':
                    number_list.append(int(i))
    return sum(number_list)

def maksimi():
    number_list = []
    with open("matriisi.txt") as tiedosto:
        for line in tiedosto:
            line = line.replace("\n", ",")
            all_numbers = line.split(",")
            for i in all_numbers:
                if i != '':
                    number_list.append(int(i))
    return max(number_list)

def rivisummat():
    row_list = []
    row_numbers = []
    row_sum = []
    with open("matriisi.txt") as tiedosto:
        for line in tiedosto:
            line = line.replace("\n", ",")
            row_list.append(line)

    index = 0
    for i in row_list:
        row_numbers.append([])
        all_numbers = i.split(",")
        for j in all_numbers:
            if j != '':
                row_numbers[index].append(int(j))
        index = index + 1
    
    for i in range(0, len(row_numbers)):
        row_sum.append(sum(row_numbers[i]))
    
    return row_sum

#osa6-04 tee ratkaisu tänne
"""
Make a program that asks for file names and then prints the total number of assignments for each student. 

Example:
Student information: students1.csv 
Assignment information: assignments1.csv 
Pekka fearless 21
"""
student_info_csvname = input("Opiskelijatiedot: ")
assignment_info_csvname = input("Tehtävätiedot: ")

with open(student_info_csvname) as tiedosto:
    next(tiedosto)
    student_id_name = {}
    for lines in tiedosto:
        lines = lines.replace("\n", "")
        student_info = lines.split(';')
        student_id_name[student_info[0]] = student_info[1] + " " + student_info[2]

with open(assignment_info_csvname) as tiedosto:
    next(tiedosto)
    student_id_assignments = {}
    for lines in tiedosto:
        lines = lines.replace("\n", "")
        student_info = lines.split(';')
        student_id_assignments[student_info[0]] = 0
        for i in student_info[1:]:
            student_id_assignments[student_info[0]] = student_id_assignments[student_info[0]] + int(i)

for key, value in student_id_name.items():
    print(value, student_id_assignments[key])

#osa6-05 tee ratkaisu tänne
"""
The previous task is further expanded so that the student's test points are also read from the CSV file.
"""
student_info_csvname = input("Opiskelijatiedot: ")
assignment_info_csvname = input("Tehtävätiedot: ")
points_info_csvname = input("Koepisteet: ")

with open(student_info_csvname) as tiedosto:
    next(tiedosto)
    student_id_name = {}
    for lines in tiedosto:
        lines = lines.replace("\n", "")
        student_info = lines.split(';')
        student_id_name[student_info[0]] = student_info[1] + " " + student_info[2]

with open(assignment_info_csvname) as tiedosto:
    next(tiedosto)
    student_id_assignments = {}
    for lines in tiedosto:
        lines = lines.replace("\n", "")
        student_info = lines.split(';')
        student_id_assignments[student_info[0]] = 0
        for i in student_info[1:]:
            student_id_assignments[student_info[0]] = student_id_assignments[student_info[0]] + int(i)

with open(points_info_csvname) as tiedosto:
    next(tiedosto)
    student_id_point = {}
    for lines in tiedosto:
        lines = lines.replace("\n", "")
        student_info = lines.split(';')
        student_id_point[student_info[0]] = 0
        for i in student_info[1:]:
            student_id_point[student_info[0]] = student_id_point[student_info[0]] + int(i)

student_assignment_point = {}
student_total_point = {}

for key, value in student_id_name.items():
    student_assignment_point[key] = student_id_assignments[key] // 4
    student_total_point[key] = student_id_assignments[key] // 4 + student_id_point[key]
    if student_total_point[key] >= 0 and student_total_point[key] <= 14:
        print(f"{value} 0")
    if student_total_point[key] >= 15 and student_total_point[key] <= 17:
        print(f"{value} 1")
    if student_total_point[key] >= 18 and student_total_point[key] <= 20:
        print(f"{value} 2")
    if student_total_point[key] >= 21 and student_total_point[key] <= 23:
        print(f"{value} 3")
    if student_total_point[key] >= 24 and student_total_point[key] <= 27:
        print(f"{value} 4")
    if student_total_point[key] >= 28:
        print(f"{value} 5")

#osa6-06 tee ratkaisu tänne
"""
Analysis and output all the infomation in the previous tasks

Examples:
nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana
pekka peloton                 21        5         9         14        	0
jaana javanainen              27        6         11        17        	1
liisa virtanen                35        8         14        22        	3
"""
if True:
    student_info_csvname = input("Opiskelijatiedot: ")
    assignment_info_csvname = input("Tehtävätiedot: ")
    points_info_csvname = input("Koepisteet: ")
else:
    student_info_csvname = "opiskelijat1.csv"
    assignment_info_csvname = "tehtavat1.csv"
    points_info_csvname = "koepisteet1.csv"

with open(student_info_csvname) as tiedosto:
    next(tiedosto)
    student_id_name = {}
    for lines in tiedosto:
        lines = lines.replace("\n", "")
        student_info = lines.split(';')
        student_id_name[student_info[0]] = student_info[1] + " " + student_info[2]

with open(assignment_info_csvname) as tiedosto:
    next(tiedosto)
    student_id_assignments = {}
    for lines in tiedosto:
        lines = lines.replace("\n", "")
        student_info = lines.split(';')
        student_id_assignments[student_info[0]] = 0
        for i in student_info[1:]:
            student_id_assignments[student_info[0]] = student_id_assignments[student_info[0]] + int(i)

with open(points_info_csvname) as tiedosto:
    next(tiedosto)
    student_id_point = {}
    for lines in tiedosto:
        lines = lines.replace("\n", "")
        student_info = lines.split(';')
        student_id_point[student_info[0]] = 0
        for i in student_info[1:]:
            student_id_point[student_info[0]] = student_id_point[student_info[0]] + int(i)

student_assignment_point = {}
student_total_point = {}

title_list = ["nimi", "teht_lkm", "teht_pist", "koe_pist", "yht_pist", "arvosana"]
print(f"{title_list[0]:<30}{title_list[1]:<10}{title_list[2]:<10}{title_list[3]:<10}{title_list[4]:<10}{title_list[5]}")
for key, value in student_id_name.items():
    student_assignment_point[key] = student_id_assignments[key] // 4
    student_total_point[key] = student_id_assignments[key] // 4 + student_id_point[key]
    if student_total_point[key] >= 0 and student_total_point[key] <= 14:
        print(f"{value:<30}{student_id_assignments[key]:<10}{student_assignment_point[key]:<10}{student_id_point[key]:<10}{student_total_point[key]:<10}0")
    if student_total_point[key] >= 15 and student_total_point[key] <= 17:
        print(f"{value:<30}{student_id_assignments[key]:<10}{student_assignment_point[key]:<10}{student_id_point[key]:<10}{student_total_point[key]:<10}1")
    if student_total_point[key] >= 18 and student_total_point[key] <= 20:
        print(f"{value:<30}{student_id_assignments[key]:<10}{student_assignment_point[key]:<10}{student_id_point[key]:<10}{student_total_point[key]:<10}2")
    if student_total_point[key] >= 21 and student_total_point[key] <= 23:
        print(f"{value:<30}{student_id_assignments[key]:<10}{student_assignment_point[key]:<10}{student_id_point[key]:<10}{student_total_point[key]:<10}3")
    if student_total_point[key] >= 24 and student_total_point[key] <= 27:
        print(f"{value:<30}{student_id_assignments[key]:<10}{student_assignment_point[key]:<10}{student_id_point[key]:<10}{student_total_point[key]:<10}4")
    if student_total_point[key] >= 28:
        print(f"{value:<30}{student_id_assignments[key]:<10}{student_assignment_point[key]:<10}{student_id_point[key]:<10}{student_total_point[key]:<10}5")

#osa6-07 tee ratkaisu tänne
"""
Make a program that asks the user to type a line of English text.
The program performs a spell check on the text and prints the same text 
so that all misspelled words are surrounded by asterisks.
The program recognizes correctly spelled words using a file in the task template wordlist.txt.
"""
sentence_list = input("Write text: ").split(" ")

with open("wordlist.txt") as tiedosto:
    word_dic = []
    for lines in tiedosto:
        lines = lines.replace("\n", "")
        word_dic.append(lines)

for i in range(0, len(sentence_list)):
    if sentence_list[i].lower() not in word_dic:
        sentence_list[i] = "*" + sentence_list[i] + "*"
    print(sentence_list[i], end = " ")
print()

#osa6-08 tee ratkaisu tänne
"""
Make a function hae_nimi(tiedosto: str, sana: str) that retrieves recipes from a file with a given parameter name
that contain a string given by another parameter.
The function returns a list in which each recipe found corresponds to a string that tells the name of the recipe.

Make a function hae_aika(tiedosto: str, aika: int) that retrieves recipes from the file with the given name
of the parameter, the preparation time of which is at most the number of minutes multiplied by the parameter.

Make a function hae_raakaaine(tiedosto: str, aine: str)that retrieves recipes from the file with the parameter
given that contain the raw material given by the second parameter.
Recipes that meet the criteria are returned to the list as in the previous task. 
"""
def file_processing(tiedosto: str):
    with open(tiedosto) as filename:
        content_list = []
        for lines in filename:
            content_list.append(lines)

    recipe_dic = {}
    for i in range(0, content_list.count("\n") + 1):
        recipe_dic[i] = []

    i = 0
    for j in content_list:
        if j == "\n":
            i = i + 1
            continue
        else:
            recipe_dic[i].append(j.strip())

    return recipe_dic

def hae_nimi(tiedosto: str, sana: str):
    recipe_search = []
    for key, value in file_processing(tiedosto).items():
        if sana.lower() in value[0].lower():
            recipe_search.append(value[0])
    return recipe_search

def hae_aika(tiedosto: str, aika: int):
    recipe_search = []
    for key, value in file_processing(tiedosto).items():
        if aika >= int(value[1]):
            recipe_search.append(f"{value[0]}, valmistusaika {value[1]} min")
    return recipe_search

def hae_raakaaine(tiedosto: str, aine: str):
    recipe_search = []
    for key, value in file_processing(tiedosto).items():
        for single_ingredient in value[2:]:
            if single_ingredient == aine:
                recipe_search.append(f"{value[0]}, valmistusaika {value[1]} min")
    return recipe_search

if __name__ == "__main__":
    loydetyt = hae_nimi("reseptit1.txt", "pulla")
    for resepti in loydetyt:
        print(resepti)

    loydetyt = hae_aika("reseptit2.txt", 20)
    for resepti in loydetyt:
        print(resepti)

    loydetyt = hae_raakaaine("reseptit2.txt", "vesi")
    for resepti in loydetyt:
        print(resepti)

#osa-09 tee ratkaisu tänne
"""
The info from the file:
Longitude;Latitude;FID;name;total_slot;operative;id
24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001

- Make a function hae_asematiedot(tiedosto: str) that reads the drive information from the file and returns
{"Kaivopuisto: (24.950292890004903, 60.155444793742276)}

- Perform a function etaisyys(asemat: dict, asema1: str, asema2: str) that reads the drive information from the file and returns
the distance between the stations multiplied by the parameter.
Calculation process:
import math
x_kilometreina = (longitude1 - longitude2) * 55.26
y_kilometreina = (latitude1 - latitude2) * 111.2
etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)

Examples:
asemat = hae_asematiedot('stations1.csv')
e = etaisyys(asemat, "Designmuseo", "Hietalahdentori")
print(e)
0.9032737292463177

- Make a function suurin_etaisyys(asemat: dict) that finds out which two stations are furthest apart.
The function returns a double whose first two values ​​tell the names of the stations and the third value the distance between them.

Examples:
asemat = hae_asematiedot('stations1.csv')
asema1, asema2, suurin = suurin_etaisyys(asemat)
print(asema1, asema2, suurin)
Laivasillankatu Hietalahdentori 1.478708873076181
"""
import math
def hae_asematiedot(tiedosto: str):
    citybike_dic = {}
    with open(tiedosto) as filename:
        next(filename)
        for lines in filename:
            lines = lines.replace("\n", "")
            citybike_info = lines.split(";")
            citybike_dic[citybike_info[3]] = (float(citybike_info[0]), float(citybike_info[1]))
    return citybike_dic

def etaisyys(asemat: dict, asema1: str, asema2: str):
    x_kilometreina = (asemat[asema1][0] - asemat[asema2][0]) * 55.26
    y_kilometreina = (asemat[asema1][1] - asemat[asema2][1]) * 111.2
    etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)
    return etaisyys

def suurin_etaisyys(asemat: dict):
    station_list = []
    for station in asemat:
        station_list.append(station)
    distance_dic = {}
    for i in range(0, len(station_list)-1):
        for j in range(i+1, len(station_list)):
            distance_dic[(station_list[i], station_list[j])] = etaisyys(asemat, station_list[i], station_list[j])
    return max(distance_dic, key = distance_dic.get)[0], max(distance_dic, key = distance_dic.get)[1], distance_dic[max(distance_dic, key = distance_dic.get)]

if __name__ == "__main__":
    asemat = hae_asematiedot('stations1.csv')

    e = etaisyys(asemat, "Designmuseo", "Hietalahdentori")
    print(e)
    e = etaisyys(asemat, "Viiskulma", "Kaivopuisto")
    print(e)

    asema1, asema2, suurin = suurin_etaisyys(asemat)
    print(asema1, asema2, suurin)

#osa6-10 tee ratkaisu tänne
"""
Write the content with inputting user_name to the file based on the inputting file_name
"""
user_name = input("Kenelle teos omistetaan: ")
file_name = input("Mihin kirjoitetaan: ")
content = "Hei " + user_name + ", toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi"
with open(file_name, "w") as tiedosto:
    tiedosto.write(content)

#osa6-11 tee ratkaisu tänne
"""
Make a program that models a simple diary.
The program should save the journal entries to a file paivakirja.txt.
When the program is started, it reads the entries from the file.
"""
while True:
    print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
    selection = int(input("Valinta: "))
    if selection == 0:
        print("Heippa!")
        break
    if selection == 1:
        with open("paivakirja.txt", "a") as tiedosto:
            tiedosto.write(input("Anna merkintä: ") + '\n')
        print("Päiväkirja tallennettu")
    if selection == 2:
        print("Merkinnät:")
        with open("paivakirja.txt") as tiedosto:
            for lines in tiedosto:
                print(lines)

#osa6-12 tee ratkaisu tänne
"""
Write a function suodata_laskut() that reads the laskut.csv contents of the file and
    - write to the file oikeat.csv the lines with the correct result of the calculation as well
    - writes to the file vaarat.csv the lines on which the result of the calculation is incorrect.
"""
def suodata_laskut():
    # Clear the content in these two files in case this function is called for multiple times
    open('oikeat.csv', 'w').close()
    open('vaarat.csv', 'w').close()
    correct_content = []
    incorrect_content = []

    with open("laskut.csv") as tiedosto:
        for line in tiedosto:
            info = line.replace("\n", "").split(";")
            if "+" in info[1]:
                info.append(info[1].split("+")[0])
                info.append(info[1].split("+")[1])
                if int(info[3]) + int(info[4]) == int(info[2]):
                    correct_content.append(info[0] + ";" + info[1] + ";" + info[2])
                else:
                    incorrect_content.append(info[0] + ";" + info[1] + ";" + info[2])

            if "-" in info[1]:
                info.append(info[1].split("-")[0])
                info.append(info[1].split("-")[1])
                if int(info[3]) - int(info[4]) == int(info[2]):
                    correct_content.append(info[0] + ";" + info[1] + ";" + info[2])
                else:
                    incorrect_content.append(info[0] + ";" + info[1] + ";" + info[2])

    with open("oikeat.csv", "w") as tiedosto:
        for info in correct_content:
            tiedosto.write(info+"\n")

    with open("vaarat.csv", "w") as tiedosto:
        for info in incorrect_content:
            tiedosto.write(info+"\n")

#osa6-13 tee ratkaisu tänne
"""
Write a function tallenna_henkilo(henkilo: tuple) that gets a tuple of the person as its parameter.
Save the person's information to a file henkilot.csva fter the existing information.
The data must be saved in the form: name, age, length
"""
def tallenna_henkilo(henkilo: tuple):
    with open("henkilot.csv", "a") as tiedosto:
        content = henkilo[0] + ";" + str(henkilo[1]) + ";" + str(henkilo[2])
        tiedosto.write(content + "\n")

if __name__ == "__main__":
    tallenna_henkilo((("Kimmo Kimmonen", 37, 175.5)))

#osa6-14 tee ratkaisu tänne
"""
Read student_info, assignment_info, exam_points and course_info from files.
After calculation and analysis, save the result to tulos.txt and tulos.csv.

The format of tulos.txt:
Ohjelmoinnin perusteet, 5 opintopistettä
========================================
nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3

The format of tulos.csv:
12345678;pekka peloton;0
12345687;jaana javanainen;1
12345699;liisa virtanen;3
"""
student_info_file = input("opiskelijatiedot: ")
assignment_info_file = input("tehtävätiedot: ")
exam_points_file = input("koepisteet: ")
course_info_file = input("kurssin tiedot: ")

student_info_dic = {} # {id: name}
with open(student_info_file) as filename:
    next(filename)
    for line in filename:
        info = line.replace("\n", "").split(";")
        student_info_dic[info[0]] = info[1] + " " + info[2]

assignment_info_dic = {} # {id: assignment_num}
with open(assignment_info_file) as filename:
    next(filename)
    for line in filename:
        info = line.replace("\n", "").split(";")
        assignment_info_dic[info[0]] = 0
        for num in info[1:]:
            assignment_info_dic[info[0]] = assignment_info_dic[info[0]] + int(num)

assignment_points_dic = {}
for key, value in assignment_info_dic.items():
    assignment_points_dic[key] = value // 4

exam_points_dic = {} # {id: exam_points}
with open(exam_points_file) as filename:
    next(filename)
    for line in filename:
        info = line.replace("\n", "").split(";")
        exam_points_dic[info[0]] = 0
        for num in info[1:]:
            exam_points_dic[info[0]] = exam_points_dic[info[0]] + int(num)

total_points_dic = {} # {id: total_points}
for key in assignment_points_dic:
    total_points_dic[key] = assignment_points_dic[key] + exam_points_dic[key]

open("tulos.txt", "w").close()
open("tulos.csv", "w").close()

course_info_list = []
with open(course_info_file) as filename:
    for line in filename:
        course_info_list.append(line.replace("\n", "").split(": ")[1])

with open("tulos.txt", "a") as filename:
    content = f"{course_info_list[0]}, {course_info_list[1]} opintopistettä"
    filename.write(content + "\n")

    isolation_line = ""
    for i in range(0, len(content)):
        isolation_line = isolation_line + "="
    filename.write(isolation_line + "\n")
    title_list = ["nimi", "teht_lkm", "teht_pist", "koe_pist", "yht_pist", "arvosana"]
    filename.write(f"{title_list[0]:<30}{title_list[1]:<10}{title_list[2]:<10}{title_list[3]:<10}{title_list[4]:<10}{title_list[5]}\n")

    for key, value in total_points_dic.items():
        if total_points_dic[key] >= 0 and total_points_dic[key] <= 14:
            filename.write(f"{student_info_dic[key]:<30}{assignment_info_dic[key]:<10}{assignment_points_dic[key]:<10}{exam_points_dic[key]:<10}{total_points_dic[key]:<10}0\n")
        if total_points_dic[key] >= 15 and total_points_dic[key] <= 17:
            filename.write(f"{student_info_dic[key]:<30}{assignment_info_dic[key]:<10}{assignment_points_dic[key]:<10}{exam_points_dic[key]:<10}{total_points_dic[key]:<10}1\n")
        if total_points_dic[key] >= 18 and total_points_dic[key] <= 20:
            filename.write(f"{student_info_dic[key]:<30}{assignment_info_dic[key]:<10}{assignment_points_dic[key]:<10}{exam_points_dic[key]:<10}{total_points_dic[key]:<10}2\n")
        if total_points_dic[key] >= 21 and total_points_dic[key] <= 23:
            filename.write(f"{student_info_dic[key]:<30}{assignment_info_dic[key]:<10}{assignment_points_dic[key]:<10}{exam_points_dic[key]:<10}{total_points_dic[key]:<10}3\n")
        if total_points_dic[key] >= 24 and total_points_dic[key] <= 27:
            filename.write(f"{student_info_dic[key]:<30}{assignment_info_dic[key]:<10}{assignment_points_dic[key]:<10}{exam_points_dic[key]:<10}{total_points_dic[key]:<10}4\n")
        if total_points_dic[key] >= 28:
            filename.write(f"{student_info_dic[key]:<30}{assignment_info_dic[key]:<10}{assignment_points_dic[key]:<10}{exam_points_dic[key]:<10}{total_points_dic[key]:<10}5\n")

with open("tulos.csv", "a") as filename:
    for key, value in total_points_dic.items():
        if total_points_dic[key] >= 0 and total_points_dic[key] <= 14:
            filename.write(f"{key};{student_info_dic[key]};0\n")
        if total_points_dic[key] >= 15 and total_points_dic[key] <= 17:
            filename.write(f"{key};{student_info_dic[key]};1\n")
        if total_points_dic[key] >= 18 and total_points_dic[key] <= 20:
            filename.write(f"{key};{student_info_dic[key]};2\n")
        if total_points_dic[key] >= 21 and total_points_dic[key] <= 23:
            filename.write(f"{key};{student_info_dic[key]};3\n")
        if total_points_dic[key] >= 24 and total_points_dic[key] <= 27:
            filename.write(f"{key};{student_info_dic[key]};4\n")
        if total_points_dic[key] >= 28:
            filename.write(f"{key};{student_info_dic[key]};5\n")

print("Tulokset talletettu tiedostoihin tulos.txt ja tulos.csv")

#osa6-15 tee ratkaisu tänne
"""
Write a function hae_sanat(hakusana: str) that returns words from the file sanat.txt that match the given keyword in the list.
Matching rules:
- A dot . means that any character goes
    - e.g., ca. matches the words cat and car, the p.ng words ping and pong, and the .a.e words sane, care, or late.
- An asterisk * means that the beginning or end of a word is any string
    - e.g., ca* corresponds to the words california, cat, caring or catapult.  *ane corresponds to crane, insane or airplane.
- If there are no special characters in the keyword, only the word that exactly matches the keyword is searched.

The words in the file are completely lowercase.
You can also assume that the function parameter is given in all lowercase.
If no results are found, the function returns an empty list.

Expected output:
['cane']
['convokes', 'equivokes', 'evokes', 'invokes', 'provokes', 'reinvokes', 'revokes']
['canine', 'canines', 'caning', 'caninity', 'canister', 'canisters']
['cannie', 'carnie', 'catnip']
"""
import re

def hae_sanat(hakusana: str):
    search_list = []

    word_list = []

    with open("sanat.txt") as filename:
        for line in filename:
            word_list.append(line.replace("\n", ""))

    if "." not in hakusana and "*" not in hakusana:
        for i in range(0, len(word_list)):
            if hakusana == word_list[i]:
                search_list.append(word_list[i])

    if "*" in hakusana:
        if hakusana.startswith("*"):
            for i in range(0, len(word_list)):
                if word_list[i].endswith(hakusana[1:]):
                    search_list.append(word_list[i])
        if hakusana.endswith("*"):
            for i in range(0, len(word_list)):
                if word_list[i].startswith(hakusana[0:-1]):
                    search_list.append(word_list[i])
  
    if "." in hakusana:
        r = re.compile(r"^%s$" % (hakusana),re.DOTALL)
        for i in range(0, len(word_list)):
            if r.search(word_list[i]) is not None:
                search_list.append(word_list[i])

    return search_list

if __name__ == "__main__":
    print(hae_sanat("cane"))
    print(hae_sanat("*vokes"))
    print(hae_sanat("cani*"))
    print(hae_sanat("ca.ni."))