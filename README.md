# Mathematical Morphology Programs
A collection of simple programs that take an image file, and apply one of the four basic morphological operators to it: erosion, dilation, opening and closing.

## Prerequisites
To use these programs, the latest version of **Python 2** needs to be installed, along with **NumPy** and **OpenCV 3.4**. The easiest way to install all of these dependencies (on a Mac) is to use the delightful Package Management Software [Homebrew](https://brew.sh/). A detailed installation tutorial can be found [here](https://www.learnopencv.com/install-opencv3-on-macos/).

## Installation
Click 'Clone or download' above and then 'Download ZIP', or alternatively run the following command from the command line:

```
git clone https://github.com/mattingram0/Mathematical-Morphology.git
```

## Running
Once downloaded (and extracted), there are four .py programs that perform each of the four morphological operations. They can be executed using the following command:

```
python [program] [input] [output]
```

where:
* \[program\] is one of erosion.py, dilation.py, closing.py or opening.py,
* \[input\] is the input image (most common image formats are supported), and 
* \[output\] is the output image.
