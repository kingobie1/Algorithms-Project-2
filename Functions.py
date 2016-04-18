# Obatola Seward-Evans
# CS 2223 Project 2
# April 17, 2016

# use Run_Fib.py brute force and recursive functions
# import numpy
import time

# - - - "BRUTE FORCE" FUNCTION - - -
def getMatrix(width, height):
    # matrix = numpy.zeros((width, height))
    matrix = {} # create matrix of dynamic size
    i = 0
    j = 0

    matrixFile = open("matrix", "r")

    for i in range(0, height):
        for j in range(0, width):
            str = matrixFile.read(2)
            str = ''.join(str.split()) # take out space and newline
            matrix[i, j] = int(str) # convert to integer and add to matrix
            print matrix[i, j]

    matrixFile.close()
    return matrix
