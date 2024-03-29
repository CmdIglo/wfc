

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

        # fetching all unique characters i.e. s, c, l, i
        for line in self.sample_img:
            for i in line:
                if i not in all_sym:
                    all_sym.append(i)
                    self.symbols.append(i)

        # now we get all the characters that can be placed next to and under and above each individual other character
        for x in range(0, len(all_sym)):
            
            sym_arr = []
            for line in range(0, len(self.sample_img)):
                
                # for every symbol in the "all_sym" array test if the symbol is in the line of the sample image
                if all_sym[x] in self.sample_img[line]:

                    # TODO: rewrite the algorithm to a simpler form, where the index of the symbol in the line is taken
                    # and add the symbols to the sym_arr which are at pos sym_index-1 and sym_index+1
                    #
                    # for every symbol in the line in the sample image 
                    for i in range(0, len(self.sample_img[line])):
                        # test if the character of the sample image is next to the the character this script is runnning for
                        if (i == self.findIndex(self.sample_img[line], all_sym[x])[0]+1 or i == self.findIndex(self.sample_img[line], all_sym[x])[0]-1) and (self.sample_img[line][i] != all_sym[x]):
                            sym_arr.append(self.sample_img[line][i])

                    # find index of the symbol in current line and append the symbols to the sym_arr which are directly adjacent to the symbol
                    # above and under the symbol
                    index_sym = self.findIndex(self.sample_img[line], all_sym[x])[0]
                    if line-1 >= 0 and (self.sample_img[line-1][index_sym] != all_sym[x]):
                        sym_arr.append(self.sample_img[line-1][index_sym])
                    if line+1 < len(self.sample_img) and (self.sample_img[line+1][index_sym] != all_sym[x]):
                        sym_arr.append(self.sample_img[line+1][index_sym])


                # check if the line, where the symbol isn't in is directly under or directly above a line, where the symbol is in

                # test the line under current line for adjacent character
                # still in development, currently built to be used as test
                # will be triggered if a line doesn't contain the character all_sym[x]
                # TODO: doesnt trigger, or I'm just dumb
                else:
                    #checks if the index tuple from the findIndex function contains values
                    if len(list(self.findIndex(self.sample_img, line))) > 0:
                        # checks if we are not on last line
                        if (self.findIndex(self.sample_img, line)[-1]+1) != len(self.sample_img)+1:
                            print(self.sample_img[self.findIndex(self.sample_img, line)[-1]], "Test")
        
            # for testing
            print(all_sym[x])
            print()

            # removing duplicate characters
            sym_arr = set(sym_arr)
            # bringing the return list into the correct form
            all_sym[x] = [all_sym[x], tuple(sym_arr)]

        return all_sym, self.symbols

    # own function for finding multiple indices of a character in a list
    def findIndex(self, arr, elem):

        indices = []

        for i in range(0, len(arr)):
            if arr[i] == elem:
                indices.append(i)

        return tuple(indices)
