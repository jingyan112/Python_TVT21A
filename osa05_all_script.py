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

Examples:
d = kertaa_kymmenen(3, 6)
print(d)

Output:
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

Examples:
k = kertomat(5)
print(k[1])
print(k[3])
print(k[5])

Output:
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

Examples:
histogrammi("abba")
histogrammi("saippuakauppias")

Output:
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