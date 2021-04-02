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
    print("starting solve")

    #initialize array which will eventually contain solution with user entries
    solving = array
    print_entries_array_to_console(solving)

    #create arrays for probability storage
    probability_array_row = [space_probabilities() for i in range(9)]
    probability_array_board = [probability_array_row for i in range(9)]

    """
    probability_array_board
    index 0   |  9 space probabilities (one probability_array_row)
    index 1   |  9 space probabilities (one probability_array_row)
    index 2   |  9 space probabilities (one probability_array_row)
    index 3   |  9 space probabilities (one probability_array_row)
    index 4   |  9 space probabilities (one probability_array_row)
    index 5   |  9 space probabilities (one probability_array_row)
    index 6   |  9 space probabilities (one probability_array_row)
    index 7   |  9 space probabilities (one probability_array_row)
    index 8   |  9 space probabilities (one probability_array_row)
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