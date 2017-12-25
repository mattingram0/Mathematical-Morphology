import numpy as np
import cv2
from sys import argv
from sys import exit


def main():

    if(len(argv) != 3):
        print '''[-] Incorrect number of arguments passed

Usage: python erosion.py [image] [output]'''
        exit(1)

    filename = argv[1]
    output = argv[2]
    parser = Parser()
    morpher = Morph()

    # Open, expand, erode and then write the image
    inImg, height, width = parser.openImage(filename)
    expImg = parser.expandImage(inImg, height, width)
    erodImg = morpher.transform("erosion", expImg, height, width)
    parser.writeImage(erodImg, output)


class Morph:
    '''Handles the mathematical morphological transformation

    Functions:
    transform() - Perform either erosion or dilation on an image'''

    def transform(self, method, image, height, width):
        '''Perform either erosion or dilation on an image

        Args:
        method - 'erosion' or 'dilation'.
        image - a NumPy array 'image'.
        height - the height of the image.
        width - the width of the image.
        Returns: a NumPy array 'image' that has been transformed'''

        transImg = np.zeros((height, width))

        for i in range(height):
            for j in range(width):
                kernel = image[i:i + 5, j:j + 5]

                if method == "erosion":
                    transImg[i, j] = np.amin(kernel)
                elif method == "dilation":
                    transImg[i, j] = np.amax(kernel)
                else:
                    print "[-] Bad Morphology - Use 'erosion' or 'dilation'"
                    exit(1)

        print "[+] " + method + " successfully applied!"
        return transImg


class Parser:
    '''Handles the opening, 'expanding' and writing of the image.

    Functions:
    openImage() - Opens an image file.
    expandImage() - Expands the boundaries of the image, using mirroring.
    writeImage() - Writes the image to a file.'''

    def openImage(self, imgFile):
        '''Opens an image file.

        Args:
        imgFile - the image file to be opened.
        Returns: NumPy array 'image' with its height and width.
        '''

        inImg = cv2.imread(imgFile, cv2.IMREAD_GRAYSCALE)
        height, width = np.shape(inImg)

        if inImg is not None:
            return inImg, height, width
        else:
            print "[-] Unable to Open Image"
            exit(1)

    def expandImage(self, inImg, height, width):
        '''Expands the boundaries of the image, using mirroring.

        Args:
        inImg - a NumPy array 'image'.
        height - the height of the image.
        width - the width of the image.
        Returns: a NumPy array representation of the expanded image.'''

        expImg = np.zeros((height + 2, width + 2))

        # Fill in the corners of the expanded image
        for i in range(2):
            for j in range(2):
                expImg[i, j] = inImg[0, 0]
                expImg[width + i, j] = inImg[0, width - 1]
                expImg[i, height + j] = inImg[0, height - 1]
                expImg[width + i, height + j] = inImg[width - 1, height - 1]

        # Fill in the borders of the expanded image
        for j in range(height):
            expImg[0, j + 2] = inImg[0, j]
            expImg[1, j + 2] = inImg[0, j]
            expImg[width, j + 2] = inImg[width - 1, j]
            expImg[width + 1, j + 2] = inImg[width - 1, j]

        # Copy in the rest of the image
        for i in range(width):
            expImg[i + 2, 0] = inImg[i, 0]
            expImg[i + 2, 1] = inImg[i, 0]
            expImg[i + 2, height] = inImg[i, height - 1]
            expImg[i + 2, height + 1] = inImg[i, height - 1]

        for i in range(height):
            for j in range(width):
                expImg[i + 2, j + 2] = inImg[i, j]

        return expImg

    def writeImage(self, image, output):
        '''A function that writes the image to a file.

        Args:
        image - the NumPy array 'image'.
        output - the output filename'''

        cv2.imwrite(output, image)


if __name__ == '__main__':
    main()
