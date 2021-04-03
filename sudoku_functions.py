import numpy as np
import sys
import space_probability_class as spc

def print_entries_array_to_console(array): #works
    a = 0
    b = 0
    while a < 9:
        while b < 9:
            print(array[a, b], end='  ')
            b += 1
        print()
        a += 1
        b = 0
    print()

def solve(array): # this is where the sudoku gets solved
    print("starting solve")

    #initialize array which will eventually contain solution with user entries
    solving = array
    print_entries_array_to_console(solving)

    #create arrays for probability storage
    probability_array_row = [spc.space_probabilities() for i in range(9)] # nine spaces per row
    probability_array_board = [probability_array_row for i in range(9)] # nine rows

    # print probability array, uses get_probability_string
    def print_probability_array_board(pab):
        for a in range(9):
            for b in range(9):
                print("| ", end='') 
                print(pab[a][b].data, end=' ')
            print("|")
        print()

    print_probability_array_board(probability_array_board)

    """
    probability_array_board
    index 0   |  9 instances of space possibility class in a list
    index 1   |  9 instances of space possibility class in a list
    index 2   |  9 instances of space possibility class in a list
    index 3   |  9 instances of space possibility class in a list
    etc...
    """

    #SOMEHOW THIS IS MAKING ALL CELLS TRUE FOR ALL POSSIBILITIES

    #store current numbers, spaces are considered all true here
    for i in range(9):
        for j in range(9):
            if solving[i][j] == 0:
                probability_array_board[i][j].clear_possibilities_to_true()
            elif solving[i][j] == 1:
                #must be 1, all other values false (ie. 0100000000)
                probability_array_board[i][j].clear_possibilities_to_false()
                probability_array_board[i][j].data[1] = 1
            elif solving[i][j] == 2:
                #must be 2, all other values false (ie. 0010000000)
                probability_array_board[i][j].clear_possibilities_to_false()
                probability_array_board[i][j].data[2] = 1
            elif solving[i][j] == 3:
                #must be 3, all other values false (ie. 0001000000)
                probability_array_board[i][j].clear_possibilities_to_false()
                probability_array_board[i][j].data[3] = 1

    # probabilities should be stored in a list of lists of classes
    # current board is in array called "solving"
    
    # test print function
    print_probability_array_board(probability_array_board)
    
