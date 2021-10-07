#osa11-19
"""
Implement a class Tehtava (task):
- with attributes: id, description, software comapny name, estimation of workload, complete_status
  - the id starts from 1 (the first task to be created gets an id of 1, the next an id of 2, etc)
  - the complete_status of the task is False at the time it is created
- the complete_status of the task can be checked with trhe method on_valmis(self)
- the complete_status of the task can be marked by calling the method merkkaa_valmiiksi(self)

Implement a class Tilauskirja which compiles all the Tehtava objects:
- lisaa_tilaus(self, kuvaus, koodari, tyomaara) method add a new order to the order book
- kaikki_tilaukset(self) method returns all tasks
- koodarit(self) method returns as a list all software comapny names in the tasks without repeating
- merkkaa_valmiiksi(self, id: int) marks the task with id as completed, if no matching, raise ValueError
- valmiit_tilaukset(self) method returns a list of complete tasks
- ei_valmiit_tilaukset(self) method returns a list of unfinished tasks
- koodarin_status(self, koodari: str) method returns a tuple of tasks with koodari, if no matching, raise ValueError
  (complete_tasks, unfinished_tasks, complete_tasks_workload, unfinished_tasks_workload)

Implement a class input_output_ui which accepts the input data from the user and error handle functions.
- 0: quit, 1: add task, 2: display complete tasks, 3: display unfinished tasks
- 4: mark task as complete, 5: display all software company names, 6: complete status of software company names
- Error checking of the input data from command 1, command 4 and command 6
"""
class id_generator:
    def __init__(self):
        self.count = 0
    
    def id_caller(self):
        self.count += 1
        return self.count

# kuvaus(description), koodari(software comapny name), tyomaara(estimation of workload)
class Tehtava:
    global id_counting
    id_counting = id_generator()

    def __init__(self, kuvaus: str, koodari: str, tyomaara: int, complete_status: bool = False):
        self.id = id_counting.id_caller()
        self.kuvaus = kuvaus
        self.koodari = koodari
        self.tyomaara = tyomaara
        self.complete_status = complete_status
    
    # Check complete_status of the task
    def on_valmis(self):
        return self.complete_status
    
    # Mark the complete_status of the task as True
    def merkkaa_valmiiksi(self):
        self.complete_status = True

    # Print task information
    def __str__(self):
        if self.on_valmis():
            return "{}: {} ({} tuntia), koodari {} VALMIS".format(self.id, self.kuvaus, self.tyomaara, self.koodari)   
        else:
            return "{}: {} ({} tuntia), koodari {} EI VALMIS".format(self.id, self.kuvaus, self.tyomaara, self.koodari)

class Tilauskirja:
    def __init__(self):
        self.task_list = []

    # Add task
    def lisaa_tilaus(self, kuvaus: str, koodari: str, tyomaara: int):
        self.task_list.append(Tehtava(kuvaus, koodari, tyomaara))
    
    # Check tasks
    def kaikki_tilaukset(self):
        return self.task_list
    
    # Check the company names in the tasks without repeating
    def koodarit(self):
        return list(set([element.koodari for element in self.task_list]))

    # Mark the complete_status of the task as True according to task id
    def merkkaa_valmiiksi(self, id: int):
        matching_times = 0
        for element in self.task_list:
            if id == element.id:
                element.merkkaa_valmiiksi()
                matching_times += 1
        if matching_times == 0:
            raise ValueError("No matching")
    
    # Check complete tasks
    def valmiit_tilaukset(self):
        return [element for element in self.task_list if element.on_valmis()]
    
    # Check unfinished tasks
    def ei_valmiit_tilaukset(self):
        return [element for element in self.task_list if not element.on_valmis()]
    
    # Check (completed_tasks, unfinished_tasks, completed_tasks_workload, unfinished_tasks_workload) according to company name
    def koodarin_status(self, koodari: str):
        matching_times = 0
        completed_tasks = 0
        completed_tasks_workload = 0
        unfinished_tasks = 0
        unfinished_tasks_workload =0

        for element in self.task_list:
            if element.koodari == koodari:
                matching_times += 1
                if element.on_valmis():
                    completed_tasks += 1
                    completed_tasks_workload += element.tyomaara
                else:
                    unfinished_tasks += 1
                    unfinished_tasks_workload += element.tyomaara
        
        if matching_times == 0:
            raise ValueError("No matching")
        else:
            return (completed_tasks, unfinished_tasks, completed_tasks_workload, unfinished_tasks_workload)

class input_output_ui:
    def __init__(self):
        self.tasks_info = Tilauskirja()

    def ui(self):
        print("komennot:")
        print("0 lopetus")                      # quit
        print("1 lisää tilaus")                 # add task
        print("2 listaa valmiit")               # display complete tasks
        print("3 listaa ei valmiit")            # display unfinished tasks
        print("4 merkitse tehtävä valmiiksi")   # mark task as complete
        print("5 koodarit")                     # software company names
        print("6 koodarin status")              # complete status of software company names
    
    # Check the format of the input data from command 1
    def error_company_workload(self, company_workload: str):
        if " " in company_workload and len(company_workload.split(" ")) == 2 and company_workload.split(" ")[1].isdigit():
            return True
        else:
            return False
    
    # Check the format of the input data from command 4
    def error_task_id(self, task_id: str):
        matching_times = 0
        if task_id.isdigit():
            for task in self.tasks_info.kaikki_tilaukset():
                if int(task_id) == task.id:
                    matching_times += 1
            if matching_times > 0:
                return True
        return False
    
    # Check the format of the input data from command 6
    def error_task_companyname(self, task_companyname: str):
        if task_companyname in self.tasks_info.koodarit():
            return True
        return False

    # Output the proper information based on the input from the user
    def command_input(self):
        self.ui()
        while True:
            print()
            command_input = int(input("komento: "))
            if command_input == 0:
                break
            elif command_input == 1:
                description = input("kuvaus: ")
                company_workload = input("koodari ja työmääräarvio: ")
                if self.error_company_workload(company_workload):
                    comapny_name = company_workload.split(" ")[0]
                    workload = int(company_workload.split(" ")[1])
                    self.tasks_info.lisaa_tilaus(description, comapny_name, workload)
                    print("lisätty!")
                else:
                    print("virheellinen syöte")
            elif command_input == 2:
                if len(self.tasks_info.valmiit_tilaukset()) == 0:
                    print("ei valmiita")
                else:
                    for task in self.tasks_info.valmiit_tilaukset():
                        print(task)
            elif command_input == 3:
                if len(self.tasks_info.ei_valmiit_tilaukset()) == 0:
                    print("ei valmiita")
                else:
                    for task in self.tasks_info.ei_valmiit_tilaukset():
                        print(task)
            elif command_input == 4:
                task_id = input("tunniste: ")
                if self.error_task_id(task_id):
                    self.tasks_info.merkkaa_valmiiksi(int(task_id))
                    print("merkitty valmiiksi")
                else:
                    print("virheellinen syöte")
            elif command_input == 5:
                for task_companyname in self.tasks_info.koodarit():
                    print(task_companyname)
            elif command_input == 6:
                task_companyname = input("koodari: ")
                if self.error_task_companyname(task_companyname):
                    result = self.tasks_info.koodarin_status(task_companyname)
                    print("työt: valmiina {} ei valmiina {}, tunteja: tehty {} tekemättä {}".format(result[0], result[1], result[2], result[3]))
                else:
                    print("virheellinen syöte")
            else:
                self.ui()

input_output_ui().command_input()