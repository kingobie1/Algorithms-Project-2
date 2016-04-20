"""
Obatola Seward-Evans
CS 2223 Project 2
April 17, 2016

helper functions:
	use Run_Matrix_Cost.py file to run the greedy and exhausted search algorithms

Problem to solve:
    You are a high-level security manager at the Gombel Security Firm. On any day you have
    access to n professional cryptographers and m messages to crack. Today, you have 4 hackers
    at your disposal and 4 intercepted messages that need to be decrypted immediately.

    Each cryptographer can only be assigned to exactly one message and exactly one message
    can be assigned to one cryptographer. Your goal is to find an assignment that minimizes
    the total cost to crack the codes. The cost matrix is below:
"""

import time # import time libray 
import itertools
matrix = {} # create matrix of dynamic size

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -




"""
getMatrix(width, height)
	int width - the width (number of columns) of the matrix in the file 'input_Matrix'
	int height - the height (number of rows) of the matrix in the file 'input_Matrix'
	return void

	creates 2d array named 'matrix' from the matrix entered in the file input_Matrix.
"""
def getMatrix(width, height):
	matrixFile = open("input_Matrix", "r")

	for h in range(0, height):
		str = matrixFile.readline()
		tempArray = str.split()
		for w in range(0, width):
			matrix[h, w] = int(tempArray[w]) # convert to integer and add to matrix

	matrixFile.close()
	return matrix




"""
exhaustiveSearch(width, height)
	int width - the width (number of columns) of the matrix in the file 'input_Matrix'
	int height - the height (number of rows) of the matrix in the file 'input_Matrix'
	return int optimalCost - returns the optimat cost determined by the greedy algorithm

	calculates the optimal cost of the matrix, solving problem listed on the top of this file.
"""
def exhaustiveSearch(width, height):
	arrayOfPerms = itertools.permutations(range(width));
	optimalCost = 9999999999

	for perm in arrayOfPerms:
		total = 0
		for index in range(0, width):
			total += matrix [ perm[index], index ]

		if total < optimalCost:
			optimalCost = total
	return optimalCost




"""
greedyAlgorithm(width, height)
	int width - the width (number of columns) of the matrix in the file 'input_Matrix'
	int height - the height (number of rows) of the matrix in the file 'input_Matrix'
	return int optimalCost - returns the optimat cost determined by the greedy algorithm

	calculates the 'optimal' cost of the matrix, solving problem listed on the top of this file.
"""

def greedyAlgorithm(width, height):
	minForRow = 9999999999
	index = 0 # where minumum row was found
	optimalCost = 0
	columnIsTaken=[0 for i in range(width)] # means taken

	for row in range (0, height):
		for col in range(0, width):
			if columnIsTaken[col] == 0: # if the column has yet to be taken
				if matrix[row, col] < minForRow: # check if it has the minimum cost
					minForRow = matrix[row, col] # if the minimum cost so far has been found change var
					index = col # compute the index where the minimum cost was found

		optimalCost += minForRow
		columnIsTaken[index] = 1 # show that columnIsTaken2[index] has been taken
		# print "    minimum for row ", row , " is: ", minForRow, " found at column: ", index, "ie coordinates [",row,",",index,"]"
		minForRow = 9999999999 # reinitialize


	return optimalCost