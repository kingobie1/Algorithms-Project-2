"""
Obatola Seward-Evans
CS 2223 Project 2
April 17, 2016

main
	The main function asks the user if he/she would like to run the exhaustive search or a 
	greedy algorithm. The function then runs either exhaustiveSearch() or greedyAlgorithm()
	which can be found in Functions.py. For both functions the time elapsed is printed.

	The user can use any matrix as he/she choses as long as he/she enters in into the
	input_Matrix file following the given format

	The two functions solve the problem below:
		You are a high-level security manager at the Gombel Security Firm. On any day you have
	    access to n professional cryptographers and m messages to crack. Today, you have 4 hackers
	    at your disposal and 4 intercepted messages that need to be decrypted immediately.

	    Each cryptographer can only be assigned to exactly one message and exactly one message
	    can be assigned to one cryptographer. Your goal is to find an assignment that minimizes
	    the total cost to crack the codes. The cost matrix is below:
"""

#!/usr/bin/python

# import the actual functions from Functions.py:
from Functions import *

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

isFirstTime = 1 # is this first time the user has been to main menu?
optimalCost = 0 # optimal cost determined by algorithms

while True:
	print "\n\n- - - MAIN MENU - - - "
	print "Select function:"
	print "  1. exhastive search"
	print "  2. greedy algorithm"
	print "  3. quit"
	option = raw_input("\n> ") # gather option value from user.

	width = 4
	height = 4
	# if isFirstTime == 1: # if first time at main menu
	#     width = input("\nwhat is the matrix width?\n> ")
	#     height = input("\nwhat is the matrix height?\n> ")

	getMatrix(width, height) # get matrix from input_Matrix file

	# run EXHASTIVE SEARCH if user selects 1st option:
	if option == "1" or option == "exhaustive search" or option == "e":
		print "\n\n- - - EXHAUSTIVE SEARCH ALGORITHM - - - "
		t0 = time.clock()  # get initial time for recursive function.
		optimalCost = exhaustiveSearch(width, height) # get optimat cost
		print "\n    The total cost using the exhaustive search algorithm is ", optimalCost
		print "    time elapsed:", (time.clock() - t0) * 1000,"millisecond\n"


	# run GREEDY ALGORITHM if user selects 2ND option:
	elif option == "2" or option == "greedy algorithm" or option == "g":
		print "\n\n- - - GREEDY ALGORITHM - - - \n"
		t1 = time.clock()  # get initial time for recursive function.
		optimalCost = greedyAlgorithm(width, height) # get optimat cost
		print "\n    The optimal cost using the greedy algorithm is ", optimalCost
		print "    time elapsed:", (time.clock() - t1) * 1000,"millisecond\n"

	# QUIT application
	elif option == "3" or option == "quit" or option == "q":
		print "\n\nIt's sad to see you go :(\n"
		break # end while loop and quit

	else:
		print "\nWrong input dude... Let's this try again :D"

	isFirstTime = 0 # no longer the first time running through the loop
	time.sleep(3) # wait 4 seconds before showing main menu again


