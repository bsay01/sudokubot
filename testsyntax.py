import numpy as np
from tkinter import *

array = np.arange(81).reshape(9, 9)

for i in array:
    for j in i:
        print(j, end = ' ')
    print()