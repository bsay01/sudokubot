from sudokubot_window1 import * #one of my files

root = Tk() # setting tkinter window
root.title('sudokubot')
root.geometry('700x700')
root.resizable(True, True)

app = sudokubot(root, 6)

root.mainloop()