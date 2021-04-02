from tkinter import *
import numpy as np
import sudoku_functions as su #one of my files

class sudokubot(Frame):
    def __init__ (self, master = None, box_size = 6):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.sidelengthboxes = box_size
        self.entries = np.arange(81).reshape(9, 9)
        self.create_widgets()

    def create_widgets(self):
        # create primary buttons and labels (not related to sudoku)
        topLabel = Label(self.master, text="add sudoku data - only numbers 1-9 will be recognized", fg="black", bg="yellow")
        solveButton = Button(self.master, text="Solve", fg="white", bg="red", command = self.get_entries)

        # pack primary buttons and labels (not related to sudoku)
        topLabel.grid(row = 0, column = 0, columnspan = 11, sticky = N)
        solveButton.grid(row = 10, column = 3, columnspan = 3, sticky = N)

        self.cells = {}
        for row in range(9):
            for column in range(9):
                textvar = StringVar()
                cell = Entry(self.master, textvariable = textvar, width = self.sidelengthboxes, justify = 'center')
                cell.grid(row=row+1, column=column, ipady=self.sidelengthboxes + 5)
                self.cells[(row, column)] = cell

    def get_entries(self):
        for row in range(9):
            for column in range(9):
                try:
                    self.entries[row, column] = int(self.cells[(row, column)].get())
                    if (self.entries[row, column] > 9) or (self.entries[row, column] < 1):
                        self.entries[row, column] = 0
                except:
                    self.entries[row, column] = 0
        #su.print_entries_array_to_console(self.entries)
        #self.user_check_input() # probably disable this honestly
        try:
            su.solve(self.entries)
        except: 
            print("sudokubot.solve(self.entries) couldn't complete. Check entries.")

    def user_check_input(self):
        # have user check their entries.
        su.print_entries_array_to_console(self.entries)