import numpy as np
import sys

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
    print("starting solve")

    #initialize array which will eventually contain solution with user entries
    solving = array
    print_entries_array_to_console(solving)

    #create arrays for probability storage
    probability_array_space = [space_probabilities() for i in range(9)] # nine possible numbers
    probability_array_row = [probability_array_space for i in range(9)] # nine rows
    probability_array_board = [probability_array_row for i in range(9)] # nine columns

    """
    probability_array_board
    index 0   |  array of 9 times 9 space probabilities (one probability_array_row)
    index 1   |  array of 9 times 9 space probabilities (one probability_array_row)
    index 2   |  array of 9 times 9 space probabilities (one probability_array_row)
    index 3   |  array of 9 times 9 space probabilities (one probability_array_row)
    index 4   |  array of 9 times 9 space probabilities (one probability_array_row)
    index 5   |  array of 9 times 9 space probabilities (one probability_array_row)
    index 6   |  array of 9 times 9 space probabilities (one probability_array_row)
    index 7   |  array of 9 times 9 space probabilities (one probability_array_row)
    index 8   |  array of 9 times 9 space probabilities (one probability_array_row)
    """

    #store current numbers, spaces are considered all true here
    for i in range(9):
        for j in range(9):
            probability_array_board[i][j].affirm( [ solving[i][j] ] ) #must pass in list

    # probabilities are in an array of arrays, type probability_array_row
    # current board is in array called "solving"
    def scan_row(row):
        numbers = []
        for i in solving[row]:
            if i != 0:
                numbers.append(i)
        return numbers
    
    def scan_column(column):
        numbers = []
        for i in solving[column]:
            if i != 0:
                numbers.append(i)
        return numbers

    # print probability array
    def print_probability_array(probability_array):
        print("| ", end='')
        a = 0
        b = 0
        while a < 9:
            while b < 9:
                #read space_probabilities into a string ex. "STFFTTTFFT", s for start string
                if probability_array_space[a][b].one == True:
                    print("1:T ", end='')
                else:
                    print("1:F ", end = '')

                if probability_array_space[a][b].two == True:
                    print("2:T ", end = '')
                else:
                    print("2:F ", end = '')
                
                if probability_array_space[a][b].three == True:
                    print("3:T ", end = '')
                else:
                    print("3:F ", end = '')

                if probability_array_space[a][b].four == True:
                    print("4:T ", end = '')
                else:
                    print("4:F ", end = "")

                if probability_array_space[a][b].five == True:
                    print("5:T ", end = "")
                else:
                    print("5:F ", end = "")
                
                if probability_array_space[a][b].six == True:
                    print("6:T ", end = "")
                else:
                    print("6:F ", end = "")

                if probability_array_space[a][b].seven == True:
                    print("7:T ", end = "")
                else:
                    print("7:F ", end = "")

                if probability_array_space[a][b].eight == True:
                    print("8:T ", end = "")
                else:
                    print("8:F ", end = "")
                
                if probability_array_space[a][b].nine == True:
                    print("9:T ", end = "")
                else:
                    print("9:F ", end = "")

                b += 1
            print("|")
            a += 1
            b = 0
        print()

    

class space_probabilities():
    def __init__ (self):
        self.one = False
        self.two = False
        self.three = False
        self.four = False
        self.five = False
        self.six = False
        self.seven = False
        self.eight = False
        self.nine = False

    def affirm(self, nums):
        try:
            for possibility in nums:
                if possibility == 0:
                    self.one = True
                    self.two = True
                    self.three = True
                    self.four = True
                    self.five = True
                    self.six = True
                    self.seven = True
                    self.eight = True
                    self.nine = True
                elif possibility == 1:
                    self.one = True
                elif possibility == 2:
                    self.two = True
                elif possibility == 3:
                    self.two = True
                elif possibility == 4:
                    self.one = True
                elif possibility == 5:
                    self.two = True
                elif possibility == 6:
                    self.two = True
                elif possibility == 7:
                    self.one = True
                elif possibility == 8:
                    self.two = True
                elif possibility == 9:
                    self.two = True
        except:
            print("ERROR: used space_probabilities.affirm wrong")

    def remove(self, nums):
        try:
            for possibility in nums:
                if possibility == 1:
                    self.one = False
                elif possibility == 2:
                    self.two = False
                elif possibility == 3:
                    self.two = False
                elif possibility == 4:
                    self.one = False
                elif possibility == 5:
                    self.two = False
                elif possibility == 6:
                    self.two = False
                elif possibility == 7:
                    self.one = False
                elif possibility == 8:
                    self.two = False
                elif possibility == 9:
                    self.two = False
        except:
            print("ERROR: used space_probabilities.remove wrong")