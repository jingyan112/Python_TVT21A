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