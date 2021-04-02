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
    solving = array
    print_entries_array_to_console(solving)
    probability_array # HERE------------------------------------------------------------------

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
                if possibility == 1:
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