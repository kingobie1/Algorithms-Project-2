# Obatola Seward-Evans
# CS 2223 Project 2
# April 17, 2016

# The main function. asks for the user if he/she would like to run the exhastive search or 
# a greedy algorithm 
# The function then runs either exhastiveSearch() or greedyAlgorithm() which can be found in 
# Functions.py. For both functions the time elapsed is printed
# [relies on the 'exhastiveSearch' and 'greedyAlgorithm' in the file Functions.py]

#!/usr/bin/python

# import the actual functions from Functions.py:
from Functions import *

count = 0
optimalCost = 0

while True:
    print "\n\n- - - MAIN MENU - - - "
    print "Select function:"
    print "  1. exhastive search"
    print "  2. greedy algorithm"
    print "  3. quit"
    option = raw_input("\n> ") # gather option value from user.

    width = 4
    height = 4
    # if count == 0: # if first time at main menu
    #     width = input("\nwhat is the matrix width?\n> ")
    #     height = input("\nwhat is the matrix height?\n> ")

    getMatrix(width, height) # get matrix from matrix file

    # run BRUTE FORCE function if user selects 1st option:
    if option == "1" or option == "exhastive search" or option == "e":
        print "\n\n- - - EXHAUSTIVE SEARCH ALGORITHM - - - "

    # run RECURSIVE function if user selects 1st option:
    elif option == "2" or option == "greedy algorithm" or option == "g":
        print "\n\n- - - GREEDY ALGORITHM - - - \n"
        optimalCost = greedyAlgorithm(width, height)
        print "\n  The optimal cost using the greedy algorithm is ", optimalCost, "\n"

    elif option == "3" or option == "quit" or option == "q":
        print "\n\nIt's sad to see you go :(\n"
        break # end while loop and quit

    else:
        print "\nWrong input dude... Let's this try again :D"

    count = 1
    time.sleep(3) # wait 4 seconds before showing main menu again


