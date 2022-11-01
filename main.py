

import random
from wfc import WFC

# importing the image-generation functions from Generator
from functions.Generator import Generator

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

# evaluating the next image-"pixel"
# recursive (?)
def evalNxt(image, pos):
    pass

# starting flag of script
if __name__ == "__main__":

    # the wave function collapse model
    model = WFC(sample_img=sample_img)

    # training the model and fetching the information list and the unique symbols of the sample image
    trained_model, symbols = model.train()

    Gen = Generator(information_list=trained_model, width=10, height=10, symbols=symbols)
    Gen.generate()