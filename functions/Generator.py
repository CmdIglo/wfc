
'''
    Generator class, implements Image Generation function
'''

import random

class Generator:
    
    def __init__(self, information_list, width, height, symbols):
        self.information_list=information_list
        self.width=width
        self.height=height
        self.symbols=symbols
        pass

    def generate(self):

        # output image
        output_img = []

        # building a list of the specified dimensions
        if self.height > 1:
            for _ in range(self.height):
                output_img.append([])
            for i in output_img:
                for _ in range(self.width):
                    i.append('P')

        # row after row will be populated
        # TODO: finish the generation algorithm -> see function "evalNxt"
        for i in range(0, len(output_img)):
            for j in range(0, len(output_img[i])):
                # first character will be chosen randomly
                if [i, j] == [0, 0]:
                    output_img[i][j] = self.symbols[random.randint(0, len(self.symbols)-1)]

        print(self.symbols)
        print()
        print(self.information_list)
        print()
        print(output_img)

        self.show(output_img)

    def show(self, image):
        
        for line in image:
            for i in range(0, len(line)):
                if i == len(line)-1:
                    print(line[i], end="\n")
                else:
                    print(line[i], end=" ")
