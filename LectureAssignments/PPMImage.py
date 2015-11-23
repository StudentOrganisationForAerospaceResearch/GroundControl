"""
2015/11/17

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
Function takes in a filename as a parameter, and then iterates accross it and imports the PPM data into a 3D list that is returned to the user
"""
# Puts the pixels of the image in the specified file in a list.  The list returned
# is a 3D list: it contains rows of pixels where each pixel is a list of length three
# containing the values for red, green and blue intensity in order.
#
# The expected format of the file is simple PPM (P3) with the added restrictions that
# - The first line has only the string P3.
# - The second line has the height and width of the pixel raster.
# - The third line has the maximum colour intensity.
# - The remaining lines each represent a single row of pixel data.
# - There are no comments in the file.
#
# Parameters:
#     ppmImageFilename: string that has the full name of the file with the ppm image data.
# Returns:
#     3D list containing the pixel raster of the image.
# Errors:
#     If the file named ppmImageFilename does not exist or the data in the file does not
#     conform to our simplified PPM image file format, the program will return an empty list.
def getPixels(ppmImageFilename):
    pixelsRaster = []
    try:
        ppmFile = open(ppmImageFilename,'r')

        #ignore first 3 lines in the ppm image file
        ppmFile.readline()
        ppmFile.readline()
        ppmFile.readline()

        # Go through the remaining lines in the file.  Each line is a row in
        # the raster.
        for line in ppmFile:
            # Each line contains all the numbers needed for the colours,  split to
            # get just the numbers.
            colourComponents = line.split()

            # Use these numbers to create a list of pixel data
            pixelRow = []

            # Each pixel is defined by three consecutive numbers.  For each iteration
            # in this loop, the index will point to the first number for a pixel.
            for index in range(0,len(colourComponents),3):
                # Each pixel has three numbers, one for red, one for green, one for blue.
                red = int(colourComponents[index])
                green = int(colourComponents[index+1])
                blue = int(colourComponents[index+2])

                # Add the data for this pixel to the row.
                pixelRow.append([red,green,blue])

            # We now have all the pixels for a row.  Add the row to the raster.
            pixelsRaster.append(pixelRow)

        ppmFile.close()
    except IOError :
        print("Encountered problem while reading data from " + ppmImageFilename)

    return pixelsRaster

# Checks if the colour specified by intensity of red, green and blue is a shade
# of green.  This assumes that red, green and blue intensity values are between
# 0 and 255.  In other words, this assumes that a colour is defined using 3 * 8 bits, or
# 24 bits.
def isGreen(red,green,blue):
    return red + 20 < green and blue + 50 < green

# Changes all green pixels in the foreground to the corresponding pixel in the background - function is pure
#
# Parameters:
#     foreground: 3d list that has all pixels in the foreground image
#     background: 3d list that has all pixels in the background image
# Returns:
#     3D list containing the pixel raster of the image.
def chromaKey(foreground, background):
    merged = []

    # loop through lines assuming the two arrays are the same.
    # Then if it's green, put in the pixel from the background,
    # else, put in the foreground pixel
    for line in range(len(foreground)):
        merged.append([])
        for pixel in range(len(foreground[line])):
            if isGreen(foreground[line][pixel][0], foreground[line][pixel][1], foreground[line][pixel][2]):
                merged[line].append(background[line][pixel])
            else:
                merged[line].append(foreground[line][pixel])

    return merged

# Creates a new ppm file and writes an image to it - function is pure
# Parameters:
#     filename: file to write to
#     image: 3d list that has all pixels to be written to file
def createPPMFile(filename, image):
    if len(image) < 1: return

    #open file if there, if not create new one
    outfile = open(filename, "w")

    #write out first three lines
    outfile.write("P3\n")
    outfile.write(str(len(image)) + " " + str(len(image[0])) + "\n")
    outfile.write("255\n")

    # Once the header data is written to the file, we can write the values for
    # the pixels a row at a time, which the following nested loop accomplishes.
    for row in image :
        for pixel in row :
            for colour in pixel :
                outfile.write(str(colour) + " ")
        outfile.write("\n")
    outfile.close()

if __name__ == "__main__" :
    foregroundPixels = getPixels("Bird.ppm")
    backgroundPixels = getPixels("Sky.ppm")
    mergedPixels = chromaKey(foregroundPixels, backgroundPixels)
    createPPMFile("BirdInSky.ppm", mergedPixels)
