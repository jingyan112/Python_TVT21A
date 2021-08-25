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
"""