

import random
from wfc import WFC

# the image the wfc "learns" from;
# simple three by three image where:
# C : coast
# S : sea
# L : land
# I : island
sample_img = [
    ['L', 'L', 'M', 'C'],
    ['M', 'L', 'C', 'S'],
    ['L', 'L', 'C', 'S'],
    ['L', 'C', 'S', 'I']
]

# all symbols of the sample image for later usage
symbols = []

# the algorithm to create a new image out of the information given from the wfc function
# takes in the information list, a width and a height (i.e. the size of the picture to be created) as arguments
# and returns a newly generated "image"
def generateImage(information_list, width, height):
    
    # initializing variables
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
    # TODO: finish the generation algorithm -> see function "evalNxt"
    for i in range(0, len(output_img)):
        for j in range(0, len(output_img[i])):
            # first character will be chosen randomly
            if [i, j] == [0, 0]:
                output_img[i][j] = symbols[random.randint(0, len(symbols)-1)]

    print(symbols)
    print()
    print(information_list)
    print()
    print(output_img)

    show(output_img)

# evaluating the next image-"pixel"
def evalNxt(image, pos):
    pass

# show the generated image
def show(image):
    for line in image:
        for i in range(0, len(line)):
            if i == len(line)-1:
                print(line[i], end="\n")
            else:
                print(line[i], end=" ")


# starting flag of script
if __name__ == "__main__":

    # the wave function collapse model
    model = WFC(sample_img=sample_img)

    # training the model and fetching the information list and the unique symbols of the sample image
    trained_model, symbols = model.train()

    # generating a new image
    # TODO: include in WFC class ?
    generateImage(trained_model, 10, 10)