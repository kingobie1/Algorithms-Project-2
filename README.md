Obatola Seward-Evans * CS 2223 Project 2

# Algorithms Project 2

## Problem: 
You are a high-level security manager at the Gombel Security Firm. On any day you have access to n professional cryptographers and m messages to crack. Today, you have 4 hackers at your disposal and 4 intercepted messages that need to be decrypted immediately.

Each cryptographer can only be assigned to exactly one message and exactly one message can be assigned to one cryptographer. Your goal is to find an assignment that minimizes the total cost to crack the codes. The cost matrix is below:

|       | MSG1 | MSG2 | MSG3 | MSG4 |
|------:|:----:|:----:|:----:|:----:|
| Jill  | 9    | 2    | 7    |   8  |
| Sven  | 6    | 4    | 3    |   7  |
| Bud   | 5    | 8    | 1    |   8  |
| Kevin | 7    | 6    | 9    |   4  |

Although you are given this small example, your code should be able to read in any n by m matrix where n and m are equal. Here are the steps to complete the project:

- Step 1. Code an exhaustive search algorithm to find the optimal solution to the above problem.

- Step 2. Code a greedy algorithm to find the optimal solution to the problem.

## Solution
The main function asks the user if he/she would like to run the exhaustive search or a greedy algorithm. The function then runs either exhaustiveSearch() or greedyAlgorithm() which can be found in Functions.py. For both functions the time elapsed is printed.

The user can use any matrix as he/she choses as long as he/she enters in into the input_Matrix file following the given format

To run, the following in your terminal:

>`$ python Run_Matrix_Cost.py`

make sure you have both files:
- Run_Fib.py
- Functions.py