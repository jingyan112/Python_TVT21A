#osa10-12
"""
Implement performance class to store the data {course1: [grade1, credit1], course2: [grade2, credit2]...}, and 
  methods for adding performance, searching performance according to course name and calculating the performance statistics
Implement user_input_output to interact with the user
- The user can add performance with command 1, only one grade is recorded for each course.
  The grade can be raised, but it cannot be lowered.
- The user can search performance according to course name with command 2
- The user can get performance statistics with command 3
- The user can quit with command 0
"""
class performance:
    def __init__(self):
        self._performance = {}
    
    def add_performance(self, course: str, grade: int, credit: int):
        if course not in self._performance:
            self._performance[course] = [grade, credit]
        else:
            if grade > self._performance[course][0]:
                self._performance[course][0] = grade
            else:
                pass
    
    def search_by_name(self, course: str):
        if course not in self._performance:
            print("ei suoritusta")
        else:
            print("Ohpe ({} op) arvosana {}".format(self._performance[course][1], self._performance[course][0]))
    
    def statistics_performance(self):
        total_grade = 0
        total_credit = 0
        grade_dic = {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0}
        for name, grade_credit in self._performance.items():
            total_grade += grade_credit[0]
            total_credit += grade_credit[1]
            if grade_credit[0] == 5:
                grade_dic["5"] += 1
            elif grade_credit[0] == 4:
                grade_dic["4"] += 1
            elif grade_credit[0] == 3:
                grade_dic["3"] += 1
            elif grade_credit[0] == 2:
                grade_dic["2"] += 1
            elif grade_credit[0] == 1:
                grade_dic["1"] += 1
            else:
                pass
        
        if len(self._performance) == 0:
            print("suorituksia 0 kurssilta, yhteensä 0 opintopistettä")
            print("keskiarvo 0")
            print("arvosanajakauma")
        else:
            print("suorituksia {} kurssilta, yhteensä {} opintopistettä".format(len(self._performance), total_credit))
            print("keskiarvo {}".format(round(total_grade/len(self._performance), 1)))
            print("arvosanajakauma")
            for grade, grade_num in grade_dic.items():
                print("{}: ".format(grade), end = "")
                for i in range(0, grade_num):
                    print("x", end = "")
                print()
    
class user_input_output:
    def __init__(self):
        self._info = performance()

    def command_ui(self):
        print("1 lisää suoritus")   # Add
        print("2 hae suoritus")     # Search
        print("3 tilastot")         # Statistics
        print("0 lopetus")          # End
    
    def input_output(self):
        self.command_ui()
        while True:
            print()
            command = int(input("komento: "))
            if command == 0:
                break
            elif command == 1:
                course = input("kurssi: ")
                grade = int(input("arvosana: "))
                credit = int(input("opintopisteet: "))
                self._info.add_performance(course, grade, credit)
            elif command == 2:
                course = input("kurssi: ")
                self._info.search_by_name(course)
            elif command == 3:
                self._info.statistics_performance()
            else:
                self.command_ui()

instance = user_input_output()
instance.input_output()

"""
Based on the following output, implement your own solution:
1 lisää suoritus
2 hae suoritus
3 tilastot
0 lopetus

komento: 1
kurssi: Ohpe
arvosana: 3
opintopisteet: 5

komento: 2
kurssi: Ohpe
Ohpe (5 op) arvosana 3

komento: 1
kurssi: Ohpe
arvosana: 5
opintopisteet: 5

komento: 2
kurssi: Ohpe
Ohpe (5 op) arvosana 5

komento: 1
kurssi: Ohpe
arvosana: 1
opintopisteet: 5

komento: 2
kurssi: Ohpe
Ohpe (5 op) arvosana 5

komento: 2
kurssi: Java-ohjelmointi
ei suoritusta

komento: 1
kurssi: Tira
arvosana: 1
opintopisteet: 10

komento: 1
kurssi: Tilpe
arvosana: 2
opintopisteet: 5

komento: 1
kurssi: Lapio
arvosana: 4
opintopisteet: 1

komento: 1
kurssi: Lama
arvosana: 5
opintopisteet: 8

komento: 3
suorituksia 5 kurssilta, yhteensä 29 opintopistettä
keskiarvo 3.4
arvosanajakauma
5: xx
4: x
3:
2: x
1: x

komento: 0
"""