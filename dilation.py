from erosion import Morph
from erosion import Parser
from sys import argv
from sys import exit


def main():

    if(len(argv) != 3):
        print '''[-] Incorrect number of arguments passed

Usage: python dilation.py [image] [output]'''
        exit(1)

    filename = argv[1]
    output = argv[2]
    parser = Parser()
    morpher = Morph()

    # Open, expand, dilate and then write the image
    inImg, height, width = parser.openImage(filename)
    expImg = parser.expandImage(inImg, height, width)
    dilateImg = morpher.transform("dilation", expImg, height, width)
    parser.writeImage(dilateImg, output)


if __name__ == '__main__':
    main()
