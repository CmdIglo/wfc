
'''
    Generator class, implements Image Generation function
'''

import random

class Generator:
    
    # information_list, list : List of every element in the sample image and its adjacent elements
    # width, int             : Width of the new image 
    # height, int            : Height of the new image
    # symbols, list          : List of all symbols in the sample image
    def __init__(self, information_list, width, height, symbols):
        self.information_list=information_list
        self.width=width
        self.height=height
        self.symbols=symbols
        self.orderedSymbols=[x[0] for x in self.information_list]
        pass

    # generates a new image from the information given in the "information-list"
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
        # TODO: finish the generation algorithm -> see function "main.evalNxt"
        for i in range(0, len(output_img)):
            for j in range(0, len(output_img[i])):
                # first character will be chosen randomly
                if [i, j] == [0, 0]:
                    output_img[i][j] = self.symbols[random.randint(0, len(self.symbols)-1)]

        print(self.symbols)
        print()
        print(self.information_list)
        print()
        for y in range(0, len(output_img)-1):
            if y == 0:
                self.evalNext((0, 0), output_img)
            else:
                self.evalNext((y, 0), output_img)
        print(output_img)

        self.show(output_img)

    # pos: tuple specifying the position for which the next values are being evaluated (y, x)
    # list: the image being generated
    # evaluates the next positions based on the current value
    def evalNext(self, pos, oList):

        y = pos[0]
        x = pos[1]
        xNext = x + 1
        yPrev = y - 1

        if y < len(oList):
            if xNext < len(oList[y]):
                # j = list of symbol and its possible neighbors
                for j in self.information_list:
                    # if the symbol is the same as the symbol for which this function is called
                    # first line
                    if oList[y][x] == j[0] and y == 0:
                        oList[y][xNext] = list(j[1])[random.randint(0, len(j[1])-1)]  
                        self.evalNext((y, xNext), oList=oList)
                    # all other lines
                    elif y != 0:
                        # first character of the line
                        if x == 0:
                            oList[y][x] = list(self.information_list[self.orderedSymbols.index(oList[yPrev][x])][1])[random.randint(0, len(self.information_list[self.orderedSymbols.index(oList[yPrev][x])][1])-1)]
                            self.evalNext((y, xNext), oList=oList)
                        else:
                            # TODO: IndexError: list index out of range line 84 > 101 > 101 > 101 > 81 > 52
                            oList[y][x] = list(self.information_list[self.orderedSymbols\
                                                .index([v for v in list(self.information_list[\
                                                self.orderedSymbols.index(oList[yPrev][x])][1]) \
                                                for w in list(self.information_list[self.orderedSymbols\
                                                .index(oList[y][x-1])][1]) if v == w][random.randint(0, \
                                                len([v for v in list(self.information_list[self.\
                                                orderedSymbols.index(oList[yPrev][x])][1]) for w in\
                                                list(self.information_list[self.orderedSymbols\
                                                .index(oList[y][x-1])][1]) if v == w])-1)])][1])[random\
                                                .randint(0, len(self.information_list[self.orderedSymbols\
                                                .index([v for v in list(self.information_list[self\
                                                .orderedSymbols.index(oList[yPrev][x])][1]) for w in \
                                                list(self.information_list[self.orderedSymbols\
                                                .index(oList[y][x-1])][1]) if v == w][random.randint(0, \
                                                len([v for v in list(self.information_list[self.orderedSymbols\
                                                .index(oList[yPrev][x])][1]) for w in list(self\
                                                .information_list[self.orderedSymbols.index(oList[y][x-1])][1]) if v == w])-1)])][1]))]
                            self.evalNext((y, xNext), oList=oList)

    # shows the generated image
    def show(self, image):
        
        for line in image:
            for i in range(0, len(line)):
                if i == len(line)-1:
                    print(line[i], end="\n")
                else:
                    print(line[i], end=" ")
