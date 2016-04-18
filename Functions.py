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
	i = 0
	j = 0

	matrixFile = open("input_Matrix", "r")

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




"""
exhaustiveSearch(width, height)
	int width - the width (number of columns) of the matrix in the file 'input_Matrix'
	int height - the height (number of rows) of the matrix in the file 'input_Matrix'
	return int optimalCost - returns the optimat cost determined by the greedy algorithm

	calculates the optimal cost of the matrix, solving problem listed on the top of this file.
"""
def exhaustiveSearch(width, height):
	return true




"""
greedyAlgorithm(width, height)
	int width - the width (number of columns) of the matrix in the file 'input_Matrix'
	int height - the height (number of rows) of the matrix in the file 'input_Matrix'
	return int optimalCost - returns the optimat cost determined by the greedy algorithm

	calculates the 'optimal' cost of the matrix, solving problem listed on the top of this file.
"""
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
		print "    minimum for row ", row , " is: ", minForRow, " found at column: ", index, "ie coordinates [",row,",",index,"]"
		minForRow = 1000000 # reinitialize


	return optimalCost