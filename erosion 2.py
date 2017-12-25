import numpy as np
import cv2

def erode(inImg):
    rows = inImg.shape[0]
    cols = inImg.shape[1]
    currentRow = 0
    currentCol = 0
    minCol1 = 255
    minCol2 = 255
    minCol3 = 255
    minCol4 = 255



#these specify the minimum grayscale values to the left and above, to saving computing speed, because just have to compare 5 values instead of 25 again to these

#creates a new, white, blank output image   
    outImg = np.zeros((rows, cols, 1) dtype = np.uint8)


    
    while currentCol != cols && currentRow != rows:
        if currentCol == cols:
            currentCol = 0
            currentRow +=1
#this if statement makes sure the 5x5 pixel mask does not go past the number of columns the image has
        else if (currentCol + 2) < cols:
            currentCol += 1
            minsArr = calcRightMins(inImg, currentRow, currentCol, minCol1, minCol2, minCol3, minCol4)
            outImg[currentRow][currentCol] = minsArr[0]
            minCol1 = minCol2
            minCol2 = minCol3
            minCol3 = minCol4
            minCol4 = minsArr[1]
#this is when the 5x5 pixel mask goes past the number of columns the image has
        else:
            currentCol += 1
            if (currentCol + 2) == cols:
                outImg[currentRow][currentCol] = calcMinsOfRowsOrCols(minCol1, minCol2, minCol3, minCol4)
            if (currentCol + 1) == cols:
                outImg[currentRow][currentCol] = calcMinsOfRowsOrCols(minCol2, minCol3, mincCol4, 255)

#This function calculates the minimum of the 4 previous rows or columns, depending on if you move right on the next pixel iteration, or down. 
#Also used initially to calculate the first 4 column minimums when at the 0,0 pixel
def calcMinsOfRowsOrCols(currentMin1, currentMin2, currentMin3, currentMin4):
    #can optimise this by using selection algorithm in theory of computation but in the meantime, uses insertion sort
    arr = [currentMin1, currentMin2, currentMin3, currentMin4];
    swap = 0
    for x in range(1,4):
        for y in range(0,x):
            if arr[x] < arr[y]:
                swap = arr[x]
                arr[x] = arr[y]
                arr[y] = swap
    return arr[0]


# This function calculates the minimum value of the neighbourhood pixels when you start a new row


def calcNewRowMin(inImg, currentRow, currentMin1, currentMin2, currentMin3, currentMin4):
    startCol = 0
    endRow = currentRow + 2
    if (currentRow -2) < 0:
        startRow = 0
    else:
        startRow = currentRow - 2
    for y in range(startCol, startCol + 3):
        for x in range(startRow, endRow + 1):



def calcRightMins(inImg, currentRow, currentCol, currentMin1, currentMin2, currentMin3, currentMin4):
# calculate minimum of 4 previous columns, and store in variable
    currentMin = calcMinsOfRowsOrCols(currentMin1, currentMin2, currentMin3, currentMin4)
#create variable that will store the minimum of the new right hand column to check
    minRightHandCols = 255
#shift column to check minimum values at the right hand most colum 
    nextCol = currentCol + 2
    currentRow -= 2
    endRow = currentRow + 4
#this sorts out the problem with the borders on the rows 
    if currentRow < 0:
        currentRow = 0
#iterates through right hand column of pixels in the 5x5 pixel mask
    while currentRow < endRow:
#finds the minimum value of the entire 5x5 pixel mask centred at the pixel in question
            if currentMin > inImg.item(currentRow, nextCol):
                currentMin = inImg.item(currentRow, nextCol)
#finds the minimum value of the right hand-most column of the 5x5 pixel mask
            if minRightHandCols > inImg.item(currentRow, nextCol):
                minRightHandCols = inImg.item(currentRow, nextCol)
        currentRow += 1
#returns both the minimum of the 5x5, and the minimum of the right hand column of the 5x5
    returnArr = [currentMin, minRightHandCols]
