from erosion import Morph
from erosion import Parser
from sys import argv
from sys import exit


def main():

    if(len(argv) != 3):
        print '''[-] Incorrect number of arguments passed

Usage: python opening.py [image] [output]'''
        exit(1)

    filename = argv[1]
    output = argv[2]
    parser = Parser()
    morpher = Morph()

    # Open, expand, erode, expand again, dilate and then write the image
    inImg, height, width = parser.openImage(filename)
    expImg = parser.expandImage(inImg, height, width)
    erodImg = morpher.transform("erosion", expImg, height, width)
    expErodImg = parser.expandImage(erodImg, height, width)
    openImg = morpher.transform("dilation", expErodImg, height, width)
    parser.writeImage(openImg, output)


if __name__ == '__main__':
    main()
