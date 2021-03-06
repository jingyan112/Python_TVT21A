#osa5-01 tee ratkaisu tänne
"""
Make a function laske_alkiot(matriisi: list, alkio: int) that takes a two-dimensional integer table as its parameter.
The function calculates how many values ​​according to a given item can be found in the table.

Expected output:
3
"""
def laske_alkiot(matriisi: list, alkio: int):
    count = 0
    for i in range(0, len(matriisi)):
        for j in range(0, len(matriisi[i])):
            if matriisi[i][j] == alkio:
                count = count + 1
    return count

if __name__ == "__main__":    
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))

#osa5-01a tee ratkaisu tänne
"""
Make a function pisin(merkkijonot: list)that gets a list of strings as its parameter.
The function finds and returns the longest string in the list.
You can assume that only one of the queues is the longest.

Expected Output:
hellurei
"""
def pisin(merkkijonot: list):
    len_dic = {}
    for i in range(0, len(merkkijonot)):
        len_dic[merkkijonot[i]] = len(merkkijonot[i])
    return max(len_dic, key = len_dic.get)

if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))

#osa5-02 tee ratkaisu tänne
"""
Write a function kumpi_voitti(pelilauta: list) that gets a two-dimensional table describing the game board as its parameter.
The table consists of integers as follows:
0: blank box
1: player's 1 piece
2: Player 2 piece
In the example, the size of the game board can be anything.
The function returns 1 if player 1 has won the game, and 2 if player 2 has won the game.
If both players have the same number of pieces on the board, the function returns 0.
"""
def kumpi_voitti(pelilauta: list):
    num_1 = 0
    num_2 = 0
    for i in range(0, len(pelilauta)):
        for j in range(0, len(pelilauta[i])):
            if pelilauta[i][j] == 1:
                num_1 = num_1 + 1
            if pelilauta[i][j] == 2:
                num_2 = num_2 + 1

    if num_1 > num_2:
        return 1
    elif num_1 < num_2:
        return 2
    else:
        return 0

#osa5-03 tee ratkaisu tänne
"""
Make a function rivi_oikein(sudoku: list, rivi_nro: int) that takes as parameters a two-dimensional table
representing the sudoku grid and an integer multiplying by the row number (rows are numbered starting from zero).
The method returns information about whether the row is filled in correctly, that is,
whether it contains each of the numbers 1 to 9 at most once.

Expected output:
True
False
"""
def rivi_oikein(sudoku: list, rivi_nro: int):
    frequency_dic = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    for i in range(0, len(sudoku[rivi_nro])):
        if sudoku[rivi_nro][i] == 1:
            frequency_dic['1'] = frequency_dic['1'] + 1
        if sudoku[rivi_nro][i] == 2:
            frequency_dic['2'] = frequency_dic['2'] + 1
        if sudoku[rivi_nro][i] == 3:
            frequency_dic['3'] = frequency_dic['3'] + 1
        if sudoku[rivi_nro][i] == 4:
            frequency_dic['4'] = frequency_dic['4'] + 1        
        if sudoku[rivi_nro][i] == 5:
            frequency_dic['5'] = frequency_dic['5'] + 1
        if sudoku[rivi_nro][i] == 6:
            frequency_dic['6'] = frequency_dic['6'] + 1
        if sudoku[rivi_nro][i] == 7:
            frequency_dic['7'] = frequency_dic['7'] + 1
        if sudoku[rivi_nro][i] == 8:
            frequency_dic['8'] = frequency_dic['8'] + 1
        if sudoku[rivi_nro][i] == 9:
            frequency_dic['9'] = frequency_dic['9'] + 1

    if frequency_dic[max(frequency_dic, key = frequency_dic.get)] > 1:
        return False
    return True

if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(rivi_oikein(sudoku, 0))
    print(rivi_oikein(sudoku, 1))

#osa5-04 tee ratkaisu tänne
"""
Make a function sarake_oikein(sudoku: list, sarake_nro: int) that takes as parameters a two-dimensional table that
represents a sudoku grid and an integer that tells you the number of a column (that is, a vertical row).
The method returns information about whether the column is filled in correctly,
that is, whether it contains each of the numbers 1 to 9 at most once.

Expected output:
False
True
"""
def sarake_oikein(sudoku: list, sarake_nro: int):
    frequency_dic = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    for i in range(0, len(sudoku)):
        if sudoku[i][sarake_nro] == 1:
            frequency_dic['1'] = frequency_dic['1'] + 1
        if sudoku[i][sarake_nro] == 2:
            frequency_dic['2'] = frequency_dic['2'] + 1
        if sudoku[i][sarake_nro] == 3:
            frequency_dic['3'] = frequency_dic['3'] + 1
        if sudoku[i][sarake_nro] == 4:
            frequency_dic['4'] = frequency_dic['4'] + 1        
        if sudoku[i][sarake_nro] == 5:
            frequency_dic['5'] = frequency_dic['5'] + 1
        if sudoku[i][sarake_nro] == 6:
            frequency_dic['6'] = frequency_dic['6'] + 1
        if sudoku[i][sarake_nro] == 7:
            frequency_dic['7'] = frequency_dic['7'] + 1
        if sudoku[i][sarake_nro] == 8:
            frequency_dic['8'] = frequency_dic['8'] + 1
        if sudoku[i][sarake_nro] == 9:
            frequency_dic['9'] = frequency_dic['9'] + 1

    if frequency_dic[max(frequency_dic, key = frequency_dic.get)] > 1:
        return False
    return True

if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sarake_oikein(sudoku, 0))
    print(sarake_oikein(sudoku, 1))

#osa5-05 tee ratkaisu tänne
"""
Make a function nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int) that takes as parameters the two-dimensional table
representing the sudoku grid and the row and column numbers that indicate the position of one square.
The function tells you whether the 3x3 square starting from the row/column number
obtained by the parameter is correctly filled, ie whether each of the numbers 1 to 9 is in it at most once.
Note that the function to be implemented in this task is a little more general than what is actually needed in sudoku.
In reality, the real sudoku only looks at (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6 , 3) and (6, 6).

Expected output:
False
True
"""
def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int):
    frequency_dic = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    
    for i in range(rivi_nro, rivi_nro+3):
        for j in range(sarake_nro, sarake_nro+3):
            if sudoku[i][j] == 1:
                frequency_dic['1'] = frequency_dic['1'] + 1
            if sudoku[i][j] == 2:
                frequency_dic['2'] = frequency_dic['2'] + 1
            if sudoku[i][j] == 3:
                frequency_dic['3'] = frequency_dic['3'] + 1
            if sudoku[i][j] == 4:
                frequency_dic['4'] = frequency_dic['4'] + 1        
            if sudoku[i][j] == 5:
                frequency_dic['5'] = frequency_dic['5'] + 1
            if sudoku[i][j] == 6:
                frequency_dic['6'] = frequency_dic['6'] + 1
            if sudoku[i][j] == 7:
                frequency_dic['7'] = frequency_dic['7'] + 1
            if sudoku[i][j] == 8:
                frequency_dic['8'] = frequency_dic['8'] + 1
            if sudoku[i][j] == 9:
                frequency_dic['9'] = frequency_dic['9'] + 1

    if frequency_dic[max(frequency_dic, key = frequency_dic.get)] > 1:
        return False
    return True

if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(nelio_oikein(sudoku, 0, 0))
    print(nelio_oikein(sudoku, 1, 2))

#osa5-06 tee ratkaisu tänne
"""
Make a function sudoku_oikein(sudoku: list) that gets a two-dimensional table representing a sudoku grid as a parameter.
Using the functions of the previous three problems (copy them to the code of this task),
the function tells whether the grid obtained by the parameter is filled correctly,
ie each row, each column and all separate 3x3 squares contain at most each of the numbers 1-9.
Note: The image above shows the 3x3 squares that should be considered when solving the sudoku grid.
These are thus from (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3 ) and (6, 6) begin at nine squares.

Expected output:
False
True
"""
def sudoku_oikein(sudoku: list):
    frequency_row_dic = {
    '0': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '1': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '2': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '3': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '4': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '5': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '6': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '7': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '8': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}}

    for i in range(0, len(sudoku)):
        for j in range(0, len(sudoku[i])):
            if sudoku[i][j] == 1:
                frequency_row_dic[str(i)]['1'] = frequency_row_dic[str(i)]['1'] + 1
            if sudoku[i][j] == 2:
                frequency_row_dic[str(i)]['2'] = frequency_row_dic[str(i)]['2'] + 1
            if sudoku[i][j] == 3:
                frequency_row_dic[str(i)]['3'] = frequency_row_dic[str(i)]['3'] + 1
            if sudoku[i][j] == 4:
                frequency_row_dic[str(i)]['4'] = frequency_row_dic[str(i)]['4'] + 1
            if sudoku[i][j] == 5:
                frequency_row_dic[str(i)]['5'] = frequency_row_dic[str(i)]['5'] + 1
            if sudoku[i][j] == 6:
                frequency_row_dic[str(i)]['6'] = frequency_row_dic[str(i)]['6'] + 1
            if sudoku[i][j] == 7:
                frequency_row_dic[str(i)]['7'] = frequency_row_dic[str(i)]['7'] + 1
            if sudoku[i][j] == 8:
                frequency_row_dic[str(i)]['8'] = frequency_row_dic[str(i)]['8'] + 1
            if sudoku[i][j] == 9:
                frequency_row_dic[str(i)]['9'] = frequency_row_dic[str(i)]['9'] + 1

    frequency_column_dic = {
    '0': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '1': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '2': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '3': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '4': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '5': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '6': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '7': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '8': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}}

    for i in sudoku:
        for j in range(0, len(i)):
            if i[j] == 1:
                frequency_column_dic[str(j)]['1'] = frequency_column_dic[str(j)]['1'] + 1
            if i[j] == 2:
                frequency_column_dic[str(j)]['2'] = frequency_column_dic[str(j)]['2'] + 1
            if i[j] == 3:
                frequency_column_dic[str(j)]['3'] = frequency_column_dic[str(j)]['3'] + 1
            if i[j] == 4:
                frequency_column_dic[str(j)]['4'] = frequency_column_dic[str(j)]['4'] + 1
            if i[j] == 5:
                frequency_column_dic[str(j)]['5'] = frequency_column_dic[str(j)]['5'] + 1
            if i[j] == 6:
                frequency_column_dic[str(j)]['6'] = frequency_column_dic[str(j)]['6'] + 1
            if i[j] == 7:
                frequency_column_dic[str(j)]['7'] = frequency_column_dic[str(j)]['7'] + 1
            if i[j] == 8:
                frequency_column_dic[str(j)]['8'] = frequency_column_dic[str(j)]['8'] + 1
            if i[j] == 9:
                frequency_column_dic[str(j)]['9'] = frequency_column_dic[str(j)]['9'] + 1

    frequency_square_dic = {
    '0': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '1': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '2': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '3': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '4': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '5': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '6': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '7': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
    '8': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}}

    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if sudoku[x][y] == 1:
                        frequency_square_dic[str(int(i+j/3))]['1'] = frequency_square_dic[str(int(i+j/3))]['1'] + 1                    
                    if sudoku[x][y] == 2:
                        frequency_square_dic[str(int(i+j/3))]['2'] = frequency_square_dic[str(int(i+j/3))]['2'] + 1 
                    if sudoku[x][y] == 3:
                        frequency_square_dic[str(int(i+j/3))]['3'] = frequency_square_dic[str(int(i+j/3))]['3'] + 1 
                    if sudoku[x][y] == 4:
                        frequency_square_dic[str(int(i+j/3))]['4'] = frequency_square_dic[str(int(i+j/3))]['4'] + 1 
                    if sudoku[x][y] == 5:
                        frequency_square_dic[str(int(i+j/3))]['5'] = frequency_square_dic[str(int(i+j/3))]['5'] + 1 
                    if sudoku[x][y] == 6:
                        frequency_square_dic[str(int(i+j/3))]['6'] = frequency_square_dic[str(int(i+j/3))]['6'] + 1 
                    if sudoku[x][y] == 7:
                        frequency_square_dic[str(int(i+j/3))]['7'] = frequency_square_dic[str(int(i+j/3))]['7'] + 1 
                    if sudoku[x][y] == 8:
                        frequency_square_dic[str(int(i+j/3))]['8'] = frequency_square_dic[str(int(i+j/3))]['8'] + 1 
                    if sudoku[x][y] == 9:
                        frequency_square_dic[str(int(i+j/3))]['9'] = frequency_square_dic[str(int(i+j/3))]['9'] + 1

    for value in frequency_row_dic.values():
        if value[max(value, key = value.get)] > 1:
            return False

    for value in frequency_column_dic.values():
        if value[max(value, key = value.get)] > 1:
            return False

    for value in frequency_square_dic.values():
        if value[max(value, key = value.get)] > 1:
            return False

    return True

if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_oikein(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_oikein(sudoku2))

#osa5-06a tee ratkaisu tänne
"""
Make a function tuplaa_alkiot(luvut: list) that gets a list of numbers as its parameter.
The function returns a new list in which the items in the original list are multiplied by two.
The function must not change the original list.

Expected output:
alkuperäinen: [2, 4, 5, 3, 11, -4]
tuplattu: [4, 8, 10, 6, 22, -8]
"""
def tuplaa_alkiot(luvut: list):
    new_luvut = []
    for i in range(0, len(luvut)):
        new_luvut.append(luvut[i]*2)
    return new_luvut

if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)

#osa5-06b tee ratkaisu tänne
"""
Make a function poista_pienin(luvut: list) that gets a list of numbers as its parameter.
The function finds and removes the smallest item from the list. You can assume that the smallest item appears in the list only once.
So the function does not return anything, but modifies the list it receives as a parameter!

Expected output:
[2, 4, 6, 3, 5]
"""
def poista_pienin(luvut: list):
    return luvut.remove(min(luvut))

if __name__ == "__main__":
    luvut = [2, 4, 6, 1, 3, 5]
    poista_pienin(luvut)
    print(luvut)

#osa5-07 tee ratkaisu tänne
"""
In this task, two more functions are implemented for sudoku: tulostaand lisays.
The function tulosta obtains a two-dimensional list representing the sudoku grid as a parameter and prints it in the format according to the example output below.
The function lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int) gets a two-dimensional list representing a sudoku grid, row and column numbers, and a number from 1 to 9.
The function inserts a sudoku grid at the point indicated by the number parameters.

Expected output:
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Kolme numeroa lisätty:

2 _ _  _ _ _  _ _ _
_ _ 7  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ 3 _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
"""
def tulosta(sudoku: list):
    for i in range(0, len(sudoku)):
        for j in range(0, len(sudoku[i])):
            if sudoku[i][j] == 0:
                print("_", end = "")
                print(" ", end = "")
            else:
                print(sudoku[i][j], end = "")
                print(" ", end = "")

            if (j+1) % 3 == 0:
                print(" ", end = "")

        if (i+1)%3 == 0:
            print()
        print()

def lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
    sudoku[rivi_nro][sarake_nro] = luku
    return sudoku

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    tulosta(sudoku)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)

#osa5-08 tee ratkaisu tänne
"""
The last task on sudoku implements a slightly different version of the function to add new numbers to the sudoku grid.
The function kopioi_ja_lisaa(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int) gets its parameters from
a two-dimensional list representing a sudoku grid, a row number, a column number, and a number between 1 and 9.
The function returns a copy of the sudoku grid obtained by the parameter,
plus the number obtained by the parameter placed at the location obtained by the parameter.
The function must not change the sudoku grid given by the parameter.

Expected output:
Alkuperäinen:
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Kopio:
2 _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Note:
All the three methods here will have an influence on the original list when trying to modify the copied list
copy_list = org_list
copy_list = org_list[:]
copy_list = list(org_list)
"""
import copy

def tulosta(sudoku: list):
    for i in range(0, len(sudoku)):
        for j in range(0, len(sudoku[i])):
            if sudoku[i][j] == 0:
                print("_", end = "")
                print(" ", end = "")
            else:
                print(sudoku[i][j], end = "")
                print(" ", end = "")

            if (j+1) % 3 == 0:
                print(" ", end = "")

        if (i+1)%3 == 0:
            print()
        print()

def kopioi_ja_lisaa(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
    sudoku_copy = copy.deepcopy(sudoku)
    sudoku_copy[rivi_nro][sarake_nro] = luku
    return sudoku_copy

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    kopio = kopioi_ja_lisaa(sudoku, 0, 0, 2)
    print("Alkuperäinen:")
    tulosta(sudoku)
    print()
    print("Kopio:")
    tulosta(kopio)

#osa5-09 tee ratkaisu tänne
"""
The cross zero is played on a 3 x 3 grid with players alternately marking a cross or zero.
The game is won by the player who gets the first three chips vertically, horizontally or at an angle.
The game ends in a draw if neither player gets three sets.
Write a function pelaa_siirto(lauta: list, x: int, y: int, nappula: str)
in which a given game piece is placed at the given coordinates on the game board.
Coordinate values ​​are between 0..2.

Note that in this task, the parameters are different from those in sudoku,
first describing the column x and then describing the row y.
The game board consists of strings as follows:
"": blank box
"X": 1 character of the player
"O": Player 2 character
The function returns a value Trueif a piece could be placed on the board (i.e., if the location was empty),
and a value Falseif the location was reserved OR if the coordinate value was too small or large (i.e., not between 0..2).

Expected output:
True
[['', '', 'X'], ['', '', ''], ['', '', '']]
"""
def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
    if y >= 0 and y <= 2 and x >= 0 and x <= 2 and lauta[y][x] != 'X' and lauta[y][x] != 'O':
        lauta[y][x] = nappula
        return True
    return False

if __name__ == "__main__":
    lauta = [['', '', 'X'], ['', '', ''], ['', '', 'O']]
    print(pelaa_siirto(lauta, 3, 0, "X"))
    print(lauta)

#osa5-10 tee ratkaisu tänne
"""
Write a function transponoi(matriisi: list) that gets a two-dimensional integer table or matrix as its parameter.
The function transposes the matrix, that is, converts the rows into columns and vice versa.
You can assume that a matrix has as many rows as there are columns (that is, the matrix is ​​a square matrix ).

Examples:
1 2 3
4 5 6
7 8 9

Output:
1 4 7
2 5 8
3 6 9
"""
def transponoi(matriisi: list):
    matriisi_copy = []
    for i in range(0,len(matriisi)):
        matriisi_copy.append([])
        for j in range(0, len(matriisi[i])):
            matriisi_copy[i].append(matriisi[i][j])

    for i in range(0, len(matriisi)):
        for j in range(0, len(matriisi[i])):
            matriisi[i][j] = matriisi_copy[j][i]

#osa5-10b tee ratkaisu tänne
"""
Make a function kertaa_kymmenen(alku: int, loppu: int) that creates and returns a new dictionary.
The dictionary contains the keys to the figures between alku.. loppu.
The value of each key is the key multiplied by ten.

Expected output:
{3:30, 4:40, 5:50, 6:60}
"""
def kertaa_kymmenen(alku: int, loppu: int):
    dic = {}
    for i in range(alku, loppu+1):
        dic[i] = i * 10
    return dic

if __name__ == "__main__":
    d = kertaa_kymmenen(3, 6)
    print(d)

#osa5-11 tee ratkaisu tänne
"""
Make a function kertomat(n: int) that returns the numbers n multiplied by the numbers 1 .. in the dictionary
so that the number is the key and the value multiplied by the number to which the key refers.
As a reminder: n told by a chapter n! is calculated by multiplying the number by any positive integer less than itself.
The multiplication of Chapter 4 is therefore 4 * 3 * 2 * 1 = 24.

Expected output:
1
6
120
"""
def kertomat(n: int):
    dic = {}
    for i in range(1, n+1):
        value = 1
        for j in range(1, i+1):
            value = value * j
        dic[i] = value
    return dic

if __name__ == "__main__":
    k = kertomat(5)
    print(k[1])
    print(k[3])
    print(k[5])

#osa5-12 tee ratkaisu tänne
"""
Make a function histogrammi that takes the parameter string and
prints a histogram of the number of different letters in the string,
with one star printed on each line of the letter.

Expected output:
a **
b **

s **
a ****
i **
p ****
u **
k *
"""
def histogrammi(string: str):
    dic = {}
    for i in range(0, len(string)):
        if string[i] not in dic:
            dic[string[i]] = string.count(string[i])
    for key, value in dic.items():
        print(key, end = " ")
        for i in range(0, value):
            print("*", end = "")
        print()

if __name__ == "__main__":
    histogrammi("abba")
    histogrammi("saippuakauppias")

#osa5-13 tee ratkaisu tänne
"""
Make a phone book that works like this:
command (1 search, 2 more, 3 stop): 2 
name: Pekka 
number: 040-5466745 
ok! 
command (1 search, 2 more, 3 stop): 1 
name: Pekka 
040-5466745
command (1 search, 2 more, 3 stop):3 
ending ...
"""
phonebook_dic = {}
while True:
    operation = int(input("komento (1 hae, 2 lisää, 3 lopeta):"))
    if operation == 1:
        name = input("nimi: ")
        if name in phonebook_dic:
            print(phonebook_dic[name])
        else:
            print("ei numeroa")

    if operation == 2:
        name = input("nimi: ")
        phonenumber = input("numero: ")
        phonebook_dic[name] = phonenumber
        print("ok!")

    if operation == 3:
        print("lopetetaan...")
        break

#osa5-14 tee ratkaisu tänne
"""
Make an enhanced version of your phonebook, where each person can have multiple phone numbers.
"""
phonebook_dic = {}
while True:
    operation = int(input("komento (1 hae, 2 lisää, 3 lopeta):"))
    if operation == 1:
        name = input("nimi: ")
        if name in phonebook_dic:
            for i in range(0, len(phonebook_dic[name])):
                print(phonebook_dic[name][i])
        else:
            print("ei numeroa")

    if operation == 2:
        name = input("nimi: ")
        phonenumber = input("numero: ")
        if name in phonebook_dic:
            phonebook_dic[name].append(phonenumber)
        else:
            phonebook_dic[name] = [phonenumber]
        print("ok!")

    if operation == 3:
        print("lopetetaan...")
        break

#osa5-15 tee ratkaisu tänne
"""
Write a function kaanna(sanakirja: dict) that gets a dictionary as its parameter and translates it
so that the values ​​become keys and vice versa.

Expected output:
{"eka": 1, "toka": 2, "kolmas": 3, "neljas": 4}
"""
def kaanna(sanakirja: dict):
    tmp_dic = {}
    for key, value in sanakirja.items():
        tmp_dic[value] = key
    sanakirja.clear() 
    for key, value in tmp_dic.items():
        sanakirja[key] = value

if __name__ == "__main__":
    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)

#osa5-16 tee ratkaisu tänne
"""
Write a function lukukirja() that returns a new dictionary.
The returned structure contains numbers from zero to 99 as keys.
The values ​​in the dictionary are numbers written in letters.

Expected output:
kaksi
yksitoista
neljäkymmentäviisi
yhdensänkymmentäyhdeksän
nolla
"""
def lukukirja():
    number_list = ["nolla", "yksi", "kaksi", "kolme", "neljä", "viisi", "kuusi", "seitsemän", "kahdeksan", "yhdeksän", "kymmenen", "yksitoista", "kaksitoista", "kolmetoista", "neljätoista", "viisitoista", "kuusitoista", "seitsemäntoista", "kahdeksantoista", "yhdeksäntoista", "kaksikymmentä", "kaksikymmentäyksi", "kaksikymmentäkaksi", "kaksikymmentäkolme", "kaksikymmentäneljä", "kaksikymmentäviisi", "kaksikymmentäkuusi", "kaksikymmentäseitsemän", "kaksikymmentäkahdeksan", "kaksikymmentäyhdeksän", "kolmekymmentä", "kolmekymmentäyksi", "kolmekymmentäkaksi", "kolmekymmentäkolme", "kolmekymmentäneljä", "kolmekymmentäviisi", "kolmekymmentäkuusi", "kolmekymmentäseitsemän", "kolmekymmentäkahdeksan", "kolmekymmentäyhdeksän", "neljäkymmentä", "neljäkymmentäyksi", "neljäkymmentäkaksi", "neljäkymmentäkolme", "neljäkymmentäneljä", "neljäkymmentäviisi", "neljäkymmentäkuusi", "neljäkymmentäseitsemän", "neljäkymmentäkahdeksan", "neljäkymmentäyhdeksän", "viisikymmentä", "viisikymmentäyksi", "viisikymmentäkaksi", "viisikymmentäkolme", "viisikymmentäneljä", "viisikymmentäviisi", "viisikymmentäkuusi", "viisikymmentäseitsemän", "viisikymmentäkahdeksan", "viisikymmentäyhdeksän", "kuusikymmentä", "kuusikymmentäyksi", "kuusikymmentäkaksi", "kuusikymmentäkolme", "kuusikymmentäneljä", "kuusikymmentäviisi", "kuusikymmentäkuusi", "kuusikymmentäseitsemän", "kuusikymmentäkahdeksan", "kuusikymmentäyhdeksän", "seitsemänkymmentä", "seitsemänkymmentäyksi", "seitsemänkymmentäkaksi", "seitsemänkymmentäkolme", "seitsemänkymmentäneljä", "seitsemänkymmentäviisi", "seitsemänkymmentäkuusi", "seitsemänkymmentäseitsemän", "seitsemänkymmentäkahdeksan", "seitsemänkymmentäyhdeksän", "kahdeksankymmentä", "kahdeksankymmentäyksi", "kahdeksankymmentäkaksi", "kahdeksankymmentäkolme", "kahdeksankymmentäneljä", "kahdeksankymmentäviisi", "kahdeksankymmentäkuusi", "kahdeksankymmentäseitsemän", "kahdeksankymmentäkahdeksan", "kahdeksankymmentäyhdeksän", "yhdeksänkymmentä", "yhdeksänkymmentäyksi", "yhdeksänkymmentäkaksi", "yhdeksänkymmentäkolme", "yhdeksänkymmentäneljä", "yhdeksänkymmentäviisi", "yhdeksänkymmentäkuusi", "yhdeksänkymmentäseitsemän", "yhdeksänkymmentäkahdeksan", "yhdeksänkymmentäyhdeksän"]
    number_dic = {}
    for i in range(0, 100):
        number_dic[i] = number_list[i]
    return number_dic

if __name__ == "__main__":
    luvut = lukukirja()
    print(luvut[2])
    print(luvut[11])
    print(luvut[45])
    print(luvut[99])
    print(luvut[0])

#osa5-17 tee ratkaisu tänne
"""
Write a function lisaa_elokuva(rekisteri: list, nimi: str, ohjaaja: str, vuosi: int, pituus: int) that adds one movie object to the movie register.
The register is implemented as a list, and each item in the list is one dictionary. The dictionary has the following keys:
name; supervisor; year; length

Expected output:
[{"name": "taken by Python", "director": "Pekka Python", "year": 2017, "length": 116}, {"name": "Python on a plane", "director": "Renny Pytholin "," year ": 2001," length ": 94}]
"""
def lisaa_elokuva(rekisteri: list, nimi: str, ohjaaja: str, vuosi: int, pituus: int):
    rekisteri.append({"nimi": nimi, "ohjaaja": ohjaaja, "vuosi": vuosi, "pituus": pituus})

if __name__ == "__main__":
    rekisteri = []
    lisaa_elokuva(rekisteri, "Pythonin viemää", "Pekka Python", 2017, 116)
    lisaa_elokuva(rekisteri, "Python lentokoneessa", "Renny Pytholin", 2001, 94)
    print(rekisteri)

#osa5-17b tee ratkaisu tänne
"""
Write a function etsi_elokuvat(rekisteri: list, hakusana: str) that handles the movie register created in the previous task.
The function creates a new list to which the movies with the keyword in the name are copied from the register.
Lowercase and uppercase letters are not marked in the search, so the keyword pajmust include both movie Tappajahaiand movie Pajatoiminnan historia.

Expected output:
[{"name": "taken by Python", "director": "Pekka Python", "year": 2017, "length": 116}, {"name": "Python on a plane", "director": "Renny Pythonen "," year ": 2001," length ": 94}]
"""
def etsi_elokuvat(rekisteri: list, hakusana: str):
    result_search = []
    for i in range(0, len(rekisteri)):
        if hakusana.lower() in rekisteri[i]["nimi"].lower():
            result_search.append(rekisteri[i])
    return result_search

if __name__ == "__main__":
    rekisteri = [{"nimi": "Pythonin viemää", "ohjaaja": "Pekka Python", "vuosi": 2017, "pituus": 116},
                {"nimi": "Python lentokoneessa", "ohjaaja": "Renny Pythonen", "vuosi": 2001, "pituus": 94},
                {"nimi": "Koodaajien yö", "ohjaaja": "M. Night Python", "vuosi": 2011, "pituus": 101}]

    lista = etsi_elokuvat(rekisteri, "python")
    print(lista)

#osa5-17c tee ratkaisu tänne
"""
Make a function tee_tuple(x: int, y: int, z: int) that generates and
returns a double of the integers it receives as a parameter
according to the following rules:
    The first element of the double is the smallest of the parameters
    The second element of the double is the largest of the parameters
    The third element of the double is the sum of the parameters

Expected output:
(-1, 5, 7)
"""
def tee_tuple(x: int, y: int, z: int):
    num0 = min([x, y, z])
    num1 = max([x, y, z])
    num2 = sum([x, y, z])
    return (num0, num1, num2)

if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))

#osa5-18 tee ratkaisu tänne
"""
Make a function vanhin(henkilot: list) that gets as a parameter a list of doubles representing persons.
The function searches for and returns the name of the oldest person.
The person duplicate first contains the person's name as a string and the second item the person's Year of Birth.

Expected output:
Maija
"""
def vanhin(henkilot: list):
    search_min = []
    for i in range(0, len(henkilot)):
        search_min.append(henkilot[i][1])
    for i in range(0, len(henkilot)):
        if henkilot[i][1] == min(search_min):
            return henkilot[i][0]

if __name__ == "__main__":
    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]

    print(vanhin(hlista))

#osa5-19 tee ratkaisu tänne
"""
Write a function vanhemmat(henkilot: list, vuosi: int) that returns a new list that stores
all the names of people born before the given year from the list of people obtained by the parameter.

Expected output:
['Arto', Maija ']
"""
def vanhemmat(henkilot: list, vuosi: int):
    search_min = []
    for i in range(0, len(henkilot)):
        if henkilot[i][1] < vuosi:
            search_min.append(henkilot[i][0])
    return search_min

if __name__ == "__main__":
    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]

    vanhemmat_henkilot = vanhemmat(hlista, 1979)
    print(vanhemmat_henkilot)

#osa5-20 tee ratkaisu tänne
"""
Implement a function to lisaa_opiskelija add a new student,
Implement a function tulosta that prints the data of one student.
Implement a function lisaa_suoritus that can be used to increase the student's course performance.
Implement a function koostethat prints a summary of student performance.

Expected output:
pekka:
 ei suorituksia
emilia:
 ei suorituksia
ei löytynyt ketään nimellä antti
"""

def lisaa_opiskelija(all_info: dict, student_name: str):
    all_info[student_name] = {}

def lisaa_suoritus(all_info: dict, student_name: str, course_grade: tuple):
    if course_grade[0] in all_info[student_name]:
        if all_info[student_name][course_grade[0]] < course_grade[1]:
            all_info[student_name][course_grade[0]] = course_grade[1]
    else:
        if course_grade[1] != 0:
            all_info[student_name][course_grade[0]] = course_grade[1]

def tulosta(all_info: dict, student_name: str):
    if student_name in all_info:
        print(student_name + ":")
        if len(all_info[student_name]) == 0:
            print(" ei suorituksia")
        else:
            print(f" suorituksia {len(all_info[student_name])} kurssilta:")

            sum = 0
            for i in all_info[student_name]:
                print(f"  {i} {all_info[student_name][i]}")
                sum = sum + all_info[student_name][i]
            
            print(f" keskiarvo {sum/len(all_info[student_name])}")
    
    else:
        print("ei löytynyt ketään nimellä " + student_name)
    
def kooste(all_info: dict):
    print(f"opiskelijoita {len(all_info)}")

    courses_num = {}
    for i in all_info:
        courses_num[i] = len(all_info[i])
    print(f"eniten suorituksia {courses_num[max(courses_num, key=courses_num.get)]} {max(courses_num, key=courses_num.get)}")

    grade_average = {}
    for i in all_info:
        sum = 0
        for j in all_info[i]:
            sum = sum + all_info[i][j]
        grade_average[i] = sum / len(all_info[i])
    print(f"paras keskiarvo {grade_average[max(grade_average, key=grade_average.get)]} {max(grade_average, key=grade_average.get)}")

if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "pekka")
    lisaa_opiskelija(opiskelijat, "emilia")
    tulosta(opiskelijat, "pekka")
    tulosta(opiskelijat, "emilia")
    tulosta(opiskelijat, "antti")

#osa5-21 Kirjoita ratkaisu tähän
"""
This section culminates in a relatively challenging problem-solving task that can be refined in many different ways.
While the task is in the chapter on doubles, doubles are hardly worth using here.
Make a program that prints a letter grid according to the examples below.
You can assume a maximum of 26 layers.

Examples:
Floors: 3

CCCCC
CBBBC
CBABC
CBBBC
CCCCC
"""
layer_letter_table = {}
for layer in range(0, 26):
    layer_letter_table[layer] = chr(int(layer + 65))

floor_number = int(input("Kerrokset: "))
letter_table = []

for i in range(0, floor_number * 2 - 1):
    letter_table.append([])
    for j in range(0, floor_number * 2 - 1):
        layer = max(abs(i - floor_number + 1), abs(j - floor_number + 1))
        letter_table[i].append(layer_letter_table[layer])

for i in letter_table:
    for j in i:
        print(j, end = "")
    print()