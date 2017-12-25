from erosion import Morph
from erosion import Parser
from sys import argv
from sys import exit


def main():

    if(len(argv) != 3):
        print '''[-] Incorrect number of arguments passed

Usage: python closing.py [image] [output]'''
        exit(1)

    filename = argv[1]
    output = argv[2]
    parser = Parser()
    morpher = Morph()

    # Open, expand, dilate, expand again, erode and then write the image
    inImg, height, width = parser.openImage(filename)
    expImg = parser.expandImage(inImg, height, width)
    dilateImg = morpher.transform("dilation", expImg, height, width)
    expDilateImg = parser.expandImage(dilateImg, height, width)
    closeImg = morpher.transform("erosion", expDilateImg, height, width)
    parser.writeImage(closeImg, output)


if __name__ == '__main__':
    main()
