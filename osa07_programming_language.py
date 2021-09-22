#osa7-18 tee ratkaisu tänne
"""
The program consists of lines, each of which is one of the following:
- PRINT [arvo]: prints the entered value
- MOV [muuttuja] [arvo]: sets the value assigned to the variable
- ADD [muuttuja] [arvo]: adds the value assigned to the variable
- SUB [muuttuja] [arvo}: subtracts the value given for the variable
- MUL [muuttuja] [arvo]: multiplies the variable by the given value
- [kohta]:: defines a point to jump from elsewhere
- JUMP [kohta]: jumps to a given position
- IF [ehto] JUMP [kohta]: if the condition applies, jump to the given position
- END: quits the program

The program is executed line by line starting from the first line.
The program ends when a command is received ENDor execution goes over the last line of the program.

Each program has 26 variables, whose names are A... Z. The value of each variable is 0 at the beginning of the program.
The notation [muuttuja] refers to such a variable.
All values ​​processed by the program are integers.
An entry [arvo] refers to either a variable or an integer value.

The entry [kohta] is the name of any item that is composed of small letters a... zand numbers 0... 9.
No two places can have the same name.

An entry [ehto] means a condition of the form [arvo] [vertailu] [arvo].
This [vertailu] is always one of the following: ==, !=, <, <=, >or >=.

Make the function suorita(ohjelma) to which the program is given in the list.
Each item in the list is one line of the program.
The function should return the PRINT results of the list all commands during program execution.

You can assume that the program assigned to the function is in the correct format,
that is, the function does not need to perform error handling.

The task is available in two points: get one point, if the commands PRINT, MOV, ADD, SUB, MULand END act, and yet another point, 
if the rest of the loop-related commands work.
"""
import string

def suorita(ohjelma1: list):
    final_list = []

    var_dic = {}
    jump_points_list = []

    index = 0
    while index < len(ohjelma1):
        instruction = ohjelma1[index].split(" ")

        # For MOV operation, store the name and value of the variables to the dic, need to check the second operation number
        if instruction[0].startswith("MOV"):
            if instruction[2] in string.ascii_uppercase and instruction[2] in var_dic:
                var_dic[instruction[1]] = int(var_dic[instruction[2]])
            else:
                var_dic[instruction[1]] = int(instruction[2])

        # For PRINT operation, get the value from the var_dic, need to check the second operation number
        if instruction[0].startswith("PRINT"):
            if instruction[1] not in var_dic:
                var_dic[instruction[1]] = 0

            if instruction[1] in string.ascii_uppercase and instruction[1] in var_dic:
                    final_list.append(var_dic[instruction[1]])
            else:
                final_list.append(int(instruction[1]))
            
        # For ADD operation, add the two numbers and store the result to the first variable, need to check the second operation number
        if instruction[0].startswith("ADD"):
            if instruction[1] not in var_dic:
                var_dic[instruction[1]] = 0
            
            if instruction[2] in string.ascii_uppercase and instruction[2] in var_dic:
                var_dic[instruction[1]] = int(var_dic[instruction[1]]) + int(var_dic[instruction[2]])
            else:
                var_dic[instruction[1]] = int(var_dic[instruction[1]]) + int(instruction[2])

        # For SUB operation, sub the two numbers and store the result to the first variable, need to check the second operation number
        if instruction[0].startswith("SUB"):
            if instruction[1] not in var_dic:
                var_dic[instruction[1]] = 0

            if instruction[2] in string.ascii_uppercase and instruction[2] in var_dic:
                var_dic[instruction[1]] = int(var_dic[instruction[1]]) - int(var_dic[instruction[2]])
            else:
                var_dic[instruction[1]] = int(var_dic[instruction[1]]) - int(instruction[2])

        # For MUL operation, mul the two numbers and store the result to the first variable, need to check the second operation number
        if instruction[0].startswith("MUL"):
            if instruction[1] not in var_dic:
                var_dic[instruction[1]] = 0

            if instruction[2] in string.ascii_uppercase and instruction[2] in var_dic:
                var_dic[instruction[1]] = int(var_dic[instruction[1]]) * int(var_dic[instruction[2]])
            else:
                var_dic[instruction[1]] = int(var_dic[instruction[1]]) * int(instruction[2])

        # JUMP operation
        if instruction[0].startswith("JUMP"):
            index = ohjelma1.index(instruction[1] + ":")

        # IF and JUMP operation
        if instruction[0].startswith("IF"):
            if instruction[1] in string.ascii_uppercase and instruction[1] in var_dic:
                number1 = int(var_dic[instruction[1]])
            else:
                number1 = int(instruction[1])
            
            if instruction[3] in string.ascii_uppercase and instruction[3] in var_dic:
                number2 = int(var_dic[instruction[3]])
            else:
                number2 = int(instruction[3])

            if instruction[2] == "==":
                if number1 == number2:
                    index = ohjelma1.index(instruction[5] + ":")
           
            if instruction[2] == "!=":
                if number1 != number2:
                    index = ohjelma1.index(instruction[5] + ":")

            if instruction[2] == "<":
                if number1 < number2:
                    index = ohjelma1.index(instruction[5] + ":")

            if instruction[2] == "<=":
                if number1 <= number2:
                    index = ohjelma1.index(instruction[5] + ":")

            if instruction[2] == ">":
                if number1 > number2:
                    index = ohjelma1.index(instruction[5] + ":")
    
            if instruction[2] == ">=":
                if number1 >= number2:
                    index = ohjelma1.index(instruction[5] + ":")

        if instruction[0].startswith("END"):
            break
        
        index = index + 1

    return final_list

if __name__ == "__main__":
    ohjelma1 = ['MOV A 1', 'MOV B 2', 'PRINT A', 'PRINT B', 'ADD A B', 'PRINT A', 'END']
    tulos = suorita(ohjelma1)
    print(tulos) # [1, 2, 3]

    ohjelma1 = ['MOV A 1', 'MOV B 10', 'alku:', 'IF A >= B JUMP loppu', 'PRINT A', 'PRINT B', 'ADD A 1', 'SUB B 1', 'JUMP alku', 'loppu:', 'END']
    tulos = suorita(ohjelma1)
    print(tulos) # [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

    ohjelma1 = ['MOV A 1', 'MOV B 1', 'alku:', 'PRINT A', 'ADD B 1', 'MUL A B', 'IF B <= 10 JUMP alku', 'END']
    tulos = suorita(ohjelma1)
    print(tulos) # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

    ohjelma1 = ['MOV N 50', 'PRINT 2', 'MOV A 3', 'alku:', 'MOV B 2', 'MOV Z 0', 'testi:', 'MOV C B', 'uusi:', 'IF C == A JUMP virhe', 'IF C > A JUMP ohi', 'ADD C B', 'JUMP uusi', 'virhe:', 'MOV Z 1', 'JUMP ohi2', 'ohi:', 'ADD B 1', 'IF B < A JUMP testi', 'ohi2:', 'IF Z == 1 JUMP ohi3', 'PRINT A', 'ohi3:', 'ADD A 1', 'IF A <= N JUMP alku']
    tulos = suorita(ohjelma1) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    print(tulos) 

    ohjelma1 = ['MOV A 1', 'MOV B 999', 'alku:', 'ADD A 1', 'SUB B 1', 'ADD C 1', 'IF A == B JUMP loppu', 'JUMP alku', 'loppu:', 'PRINT C']
    tulos = suorita(ohjelma1)
    print(tulos) # [499]