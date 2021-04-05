class space_probabilities():
    def __init__ (self):
        #10 indeces so possibility can be adressed by index
        #so if <space_probabilities instance>.data[3] == 1 is True, then the cell could be a 3
        self.data = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def get_probability_string(self):
        return_string = ""
        for n in self.data:
            return_string += str(n)
        return return_string
    
    def clear_possibilities_to_false(self):
        self.data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def clear_possibilities_to_true(self):
        self.data = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]