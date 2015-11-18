"""
2015/11/17

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
Function takes in a filename as a parameter, and then iterates accross it and imports the PPM data into a 3D list that is returned to the user
"""

# Function to get all the pixels and store it in a 3d array.
# It first reads all the lines from the inputted ppm file,
# then loops through all the lines to split the lines into
# bunches of three colour codes, or individual pixels.
# It then returns a 3d list of all of the pixels.
# Params:
#   inputFileName - PPM File to be read ***Assumes file is in same directory***
# Return:
#   a 3d list of the image. The list goes [image][line][pixel]
def getPixels(inputFileName):
    ppmFile = open(inputFileName, "r")
    ppmFile.readline()
    imageDimensions = ppmFile.readline().split()
    ppmFile.readline()
    lines = []
    image = []

    # Loop through and collect all lines in a list
    for pixelCounter in range(int(imageDimensions[0])):
        lines.append(ppmFile.readline().split())
    ppmFile.close()

    # Loop through and take all of these lines and split it into pixels, store in a different 3d array
    for line in range(len(lines)):
        image.append([])

        for value in range(0,len(lines[line]),3):
            image[line].append([lines[line][value], lines[line][value + 1], lines[line][value + 2]])

    return image
