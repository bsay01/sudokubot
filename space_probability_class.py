class space_probabilities():
    def __init__ (self):
        #remember that index refers to value one more than it, ex. index 0 stores whether a space can be 1 or not
        self.data = [1, 1, 1, 1, 1, 1, 1, 1, 1]

    def get_probability_string(self):
        return_string = ""
        for n in self.data:
            return_string += str(n)
        return return_string
    
    def get_probability_list(self): #return a copy of data
        return_list = self.data
        return return_list

    def clear_possibilities_to_false(self):
        self.data = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def clear_possibilities_to_true(self):
        self.data = [1, 1, 1, 1, 1, 1, 1, 1, 1]

    def confirm_possibility(self, num): #function does not change possibility of any value other than the one it is given
        if num > 0 and num < 10:
            #confirm possibility. see __init__ about why there's a -1 in here
            self.data[num - 1] = 1
            return True
        else:
            #function was passed an invalid value for sudoku (not 1-9)
            return False

    def remove_possibility(self, num): #function does not change possibility of any value other than the one it is given
        if num > 0 and num < 10:
            #remove possibility. see __init__ about why there's a -1 in here
            self.data[num - 1] = 0
            return True
        else:
            #function was passed an invalid value for sudoku (not 1-9)
            return False