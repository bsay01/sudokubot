import numpy as np

def print_entries_array_to_console(array):
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
    print_entries_array_to_console(array)

    print("starting solve")

    solved = array

