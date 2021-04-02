# File structure

This project is divided into a few files - so far, one for sudoku functions, one for opening and managing the tkinter
window, and one file used to start the entire project up.

**Requirements:**
Machine needs python==3.9.2, whatever version of tkinter was latest on December 14 2020,
and numpy==1.19.4. These requirements are as of April 2nd 2021.

## main.py
This is the file to run to start up the entire app. It first sets up the tkinter window, then starts up
an instance of the sudokubot class from sudokubot_window1.py. Afterwards, it runs the tkinter mainloop() method.

## sudokubot_window1.py
This is only called window "1" because I anticipate having to use more windows at some point and i'm not good enough 
at tkinter yet to know how to do that. The get_entries method calls the solve method from sudoku_functions.py, which as 
expected, will hopefully solve the given sudoku.

## sudoku_functions.py
So far this contains two methods, one to print the data array containing all of the sudoku values and a solve method,
which will probably call more future functions contained in this file.

# Future
Solve method in sudoku_functions.py needs to be completed, and there needs to be a way to display the final product in the tkinter window.
Preferably the same window, because I want the user to be able to see the solution and entering a new sudoku to be 
solved at the same time. Maybe add a second sudoku graph to the right of the input graph to display the solution?

Avoid having seperate arrays in solve method for speed's sake. Python is already slow.

Make sure that the display of the solution is actively updating as the program is working. 
Might require a new method in sudokubot_window1, but I don't know. 
Showing live solution is more important for this project than speed, but I still want to make it as fast as possible.