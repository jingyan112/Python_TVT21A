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