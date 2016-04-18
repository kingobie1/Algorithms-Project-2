# Obatola Seward-Evans
# CS 2223 Project 2
# April 17, 2016

# use Run_Fib.py brute force and recursive functions
# import numpy
import time
matrix = {} # create matrix of dynamic size

# - - - "BRUTE FORCE" FUNCTION - - -
def getMatrix(width, height):
    # matrix = numpy.zeros((width, height))
    # matrix = {} # create matrix of dynamic size
    i = 0
    j = 0

    matrixFile = open("matrix", "r")

    for h in range(0, height):
        str = matrixFile.readline()
        tempArray = str.split()
        for w in range(0, width):
            # str = matrixFile.read(2)
            # str = ''.join(str.split()) # take out space and newline
            # matrix[i, j] = int(str) # convert to integer and add to matrix
            matrix[h, w] = int(tempArray[w]) # convert to integer and add to matrix
            # print matrix[h, w]

    matrixFile.close()
    return matrix

def greedyAlgorithm(width, height):
    minForRow = 1000000
    index = 0
    optimalCost = 0
    takenColumns=[0 for i in range(width)] # means taken

    for row in range (0, height):
        for col in range(0, width):
            if takenColumns[col] == 0: # if the column has yet to be taken
                if matrix[row, col] < minForRow: # check if it has the minimum cost
                    minForRow = matrix[row, col] # if the minimum cost so far has been found change var
                    index = col # compute the index where the minimum cost was found

        optimalCost += minForRow
        takenColumns[index] = 1 # show that takenColumns[index] has been taken
        print "  minimum for row ", row , " is: ", minForRow, " found at column: ", index, "ie coordinates [",row,",",index,"]"
        minForRow = 1000000 # reinitialize


    return optimalCost