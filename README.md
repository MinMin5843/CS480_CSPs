# Overview
This project utilizes backtracking in two ways to solve Sudoku puzzles through both naive and smart algorithms. The following tasks were followed:
1. For the naive backtracking algorithm, the selection of variables and assignment of values can be done either in order or randomly.
2. For the smart backtracking algorithm, the smart variable and value orderings strategies were in incorporated in the form of the minimum remaining values (MRV), least constraining value (LCV), and forward checking (FC). 

## How to run the program
1. Run the following command in the terminal:
    ```bash
    python sudoku_main.py
2. Follow the prompts for:
    - entering the filepath to the Sudoku puzzle (examples: data/easy_1.txt OR data/medium_2.txt)
    - entering which solver to use where you can choose between the naive or smart solvers
