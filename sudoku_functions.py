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

#function to return list of values in the same box as a given index of a sudoku-sized array


#function to return list of values in the same row as a given index of a sudoku-sized array


#function to return list of values in the same col as a given index of a sudoku-sized array


def solve(array): # this is where the sudoku gets solved
    print("starting solve")

    #initialize array which will eventually contain solution with user entries
    solving = array
    print("current board as array of integers:")
    print_entries_array_to_console(solving)

    #create arrays for probability storage
    probability_array_board = [[spc.space_probabilities() for i in range(9)] for j in range(9)] # nine spaces per row

    # print probability array, uses get_probability_string
    def print_probability_array_board(pab):
        for a in range(9):
            for b in range(9):
                print("[", end = '')
                print(pab[a][b].get_probability_string(), end = '')
                print("] ", end = '')
            print()
        print()

    """
    probability_array_board
    index 0   |  9 instances of space possibility class in a list
    index 1   |  9 instances of space possibility class in a list
    index 2   |  9 instances of space possibility class in a list
    index 3   |  9 instances of space possibility class in a list
    etc...
    """

    print("Probability array after creation:")
    print_probability_array_board(probability_array_board)

    #store current numbers in probability array, spaces are considered all true here
    
    #create list of tuples (value, row, column) for values != 0 in solving
    values = []
    for i in range(9):
        for j in range(9):
            if solving[i][j] != 0:
                values.append( (solving[i][j], i, j) )

    print("nonzero values and indeces in current sudoku: ")
    print(values)
    print()

    #run through list of tuples, changing probability array for every index of values
    for nonzero in values:
        print("tuple being stored:", end = ' ')
        print(nonzero)
        probability_array_board[nonzero[1]][nonzero[2]].clear_possibilities_to_false()
        probability_array_board[nonzero[1]][nonzero[2]].confirm_possibility( nonzero[0] )
        print_probability_array_board(probability_array_board)

    # probabilities should be stored in a list of lists of classes
    # current board is in array called "solving"
    
    # test print function
    print("probability array after storing given values: ")
    print_probability_array_board(probability_array_board)

    """ time to update probability array for empty spaces based on the given values around them """
    #functions to this end (detecting values in the same row, column, and box)

