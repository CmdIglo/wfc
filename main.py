

import random

# the image the wfc "learns" from;
# simple three by three image where:
# c : coast
# s : sea
# l : land
sample_img = [
    ['L', 'L', 'M', 'C'],
    ['M', 'L', 'C', 'S'],
    ['L', 'L', 'C', 'S'],
]

# all symbols of the sample image for later usage
symbols = []

# wave function collapse function, the "learning" algorithm
# takes in a sample image as variable and returns the information list, or "trained model" if you want to say it 
# in machine learning terms
def wfc(sample_img):

    # the list where the information will be stored in
    # looks like: [[letter, (letter that can come, next, to it)]] in the end
    all_sym = []

    # fetching all unique characters i.e. s, c, l
    for line in sample_img:
        for i in line:
            if i not in all_sym:
                all_sym.append(i)
                symbols.append(i)

    # now we get all the characters that can be placed next to each individual other character
    for x in range(0, len(all_sym)):
        sym_arr = []
        for line in sample_img:
            if all_sym[x] in line:
                for i in range(0, len(line)):
                    if i == findIndex(line, all_sym[x])[0]+1 or i == findIndex(line, all_sym[x])[0]-1:
                        sym_arr.append(line[i])
            else:
                continue

        # removing duplicate characters
        sym_arr = set(sym_arr)
        # bringing the return list into the correct form
        all_sym[x] = [all_sym[x], tuple(sym_arr)]

    return all_sym

# own function for finding multiple indices of a character in a list
def findIndex(arr, elem):
    
    indices = []

    for i in range(0, len(arr)):
        if arr[i] == elem:
            indices.append(i)

    return tuple(indices)

# the algorithm to create a new image out of the information given from the wfc function
# takes in the information list, a width and a height (i.e. the size of the picture to be created) as arguments
# and returns a newly generated "image"
def generateImage(information_list, width, height):
    information_list=information_list
    width=width
    height=height

    # output image
    output_img = []

    # building a list of the specified dimensions
    if height > 1:
        for _ in range(height):
            output_img.append([])
        for i in output_img:
            for _ in range(width):
                i.append('P')

    # row after row will be populated
    for i in range(0, len(output_img)):
        for j in range(0, len(output_img[i])):
            # first character will be chosen randomly
            if [i, j] == [0, 0]:
                output_img[i][j] = symbols[random.randint(0, len(symbols))]

    print(symbols)
    print()
    print(information_list)
    print()
    print(output_img)

# starting flag of script
if __name__ == "__main__":
    #print(wfc(sample_img=sample_img))
    generateImage(wfc(sample_img=sample_img), 2, 2)