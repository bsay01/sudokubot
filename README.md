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
at tkinter yet to know how to do that. The get_entries method calls the solve method from sudoku_functions.py, which will hopefully solve the given sudoku.

## sudoku_functions.py
So far this contains a few methods: 
 - print the data array containing all of the sudoku values
 - return list of values in the same box as a given index of a sudoku-sized array (in progress)
 - return list of values in the same row as a given index of a sudoku-sized array (in progress)
 - return list of values in the same col as a given index of a sudoku-sized array (in progress)

## space_probability_class.py
So far this contains a class used in sudoku_functions.py that contains the list of possible values for that space and a couple methods to use that list.

# Future

Next work:
 - finish functions specified above in the sudoku_functions.py section
 - continue solve method, first using those functions to update the probabilities of all empty spaces of the sudoku
 - make a shell script to run the program, so that the app can be run with ./<shell script> rather than an entire python command

Solve method in sudoku_functions.py needs to be completed, and there needs to be a way to display the final product in the tkinter window.
Preferably the same window, because I want the user to be able to see the solution and entering a new sudoku to be 
solved at the same time. Maybe add a second sudoku graph to the right of the input graph to display the solution.

Try to have as few arrays as possible to update in solve method for speed's sake. Python is already slow.

Make sure that the display of the solution is actively updating as the program is working. 
Might require a new "update window with values" method in sudokubot_window1, but I don't know. 
Showing live solution is more important for this project than speed, but I still want to make it as fast as possible.

At the end of the project, make sure to update all import statements to only include methods that we use.
