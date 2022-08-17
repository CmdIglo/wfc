

import random

# wave function collapse class
class WFC():
    
    # initializing the class by passing in a sample image
    def __init__(self, sample_img):
        # initializing the variables
        self.sample_img = sample_img
        symbols = []
        self.symbols = symbols

    # "training" the WFC model
    def train(self):
        
        # the list where the information will be stored in
        # looks like: [[letter, (letter that can come, next, to it)]] in the end
        all_sym = []

        # fetching all unique characters i.e. s, c, l
        for line in self.sample_img:
            for i in line:
                if i not in all_sym:
                    all_sym.append(i)
                    self.symbols.append(i)

        # now we get all the characters that can be placed next to and under and above each individual other character
        for x in range(0, len(all_sym)):
            
            sym_arr = []
            for line in self.sample_img:
                
                # for every symbol in the "all_sym" array test if the symbol is in the line of the sample image
                if all_sym[x] in line:
                    # for every symbol in the line in the sample image 
                    for i in range(0, len(line)):
                        # test if the character of the sample image is next to the the character this script is runnning for
                        if i == self.findIndex(line, all_sym[x])[0]+1 or i == self.findIndex(line, all_sym[x])[0]-1:
                            sym_arr.append(line[i])

                # test the line under current line for adjacent character
                # still in development, currently built to be used as test
                else:
                    if (self.findIndex(self.sample_img, line)[-1]+1) != len(self.sample_img)+1:
                        print(self.sample_img[self.findIndex(self.sample_img, line)[-1]], "Test")
        
            # for testing
            print(all_sym[x])
            print()

            # removing duplicate characters
            sym_arr = set(sym_arr)
            # bringing the return list into the correct form
            all_sym[x] = [all_sym[x], tuple(sym_arr)]

        # for testing
        print("-----------------")

        return all_sym, self.symbols

    # own function for finding multiple indices of a character in a list
    def findIndex(self, arr, elem):

        indices = []

        for i in range(0, len(arr)):
            if arr[i] == elem:
                indices.append(i)

        return tuple(indices)