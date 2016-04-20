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
	matrixFile = open("input_Matrix", "r") # open the file input_Matrix.

	# for each line in the file:
	for h in range(0, height):
		str = matrixFile.readline() # put the line into string str.
		tempArray = str.split() # split the line by spaces and put each number in array.

		# for each value:
		for w in range(0, width):
			matrix[h, w] = int(tempArray[w]) # convert to integer and add to matrix.

	matrixFile.close() # close file.
	return matrix # return the matrix.




"""
exhaustiveSearch(width, height)
	int width - the width (number of columns) of the matrix in the file 'input_Matrix'
	int height - the height (number of rows) of the matrix in the file 'input_Matrix'
	return int optimalCost - returns the optimat cost determined by the greedy algorithm

	calculates the optimal cost of the matrix, solving problem listed on the top of this file.
"""
def exhaustiveSearch(width, height):
	# get every permutation of 0 to width:
	arrayOfPerms = itertools.permutations(range(width)) # produces permutations such as [[0 1], [1 0]].
	optimalCost = 9999999999 # optimal cost for all permutations.

	# for each permuation in all permutations:
	for perm in arrayOfPerms:
		totalCost = 0 # initialize total cost value for that permutation.

		# for  each index of the permutation:
		for index in range(0, width):
			totalCost += matrix [ perm[index], index ] # add to the total cost value.

		# if new optimal cost is found:
		if totalCost < optimalCost:
			optimalCost = totalCost # update optimal cost.

	return optimalCost




"""
greedyAlgorithm(width, height)
	int width - the width (number of columns) of the matrix in the file 'input_Matrix'
	int height - the height (number of rows) of the matrix in the file 'input_Matrix'
	return int optimalCost - returns the optimat cost determined by the greedy algorithm

	calculates the 'optimal' cost of the matrix, solving problem listed on the top of this file.
"""
def greedyAlgorithm(width, height):
	minForRow = 9999999999 # minimum cost for each row.
	index = 0 # where minumum row was found.
	optimalCost = 0 # optimal cost for the matrix.

	# identify which message/column is taken:
	columnIsTaken=[0 for i in range(width)] # 0 false, 1 true.

	# for each row in the matrix:
	for row in range (0, height):

		# for each column in the matrix:
		for col in range(0, width):

			# if message/column is not yet taken by a cryptographer/row:
			if columnIsTaken[col] == 0:

				# the cost for decryption is the smallest cost for the cryptographer/row:
				if matrix[row, col] < minForRow:
					minForRow = matrix[row, col] # update the minimum cost.
					index = col # compute the index where the minimum cost was found.

		optimalCost += minForRow # update the total min cost with the min cost for row.
		columnIsTaken[index] = 1 # update that the message/column, index, has been taken.
		# print "    minimum for row ", row , " is: ", minForRow, " found at column: ", index, "ie coordinates [",row,",",index,"]"
		minForRow = 9999999999 # reinitialize the minimum value for the row.


	return optimalCost