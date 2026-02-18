class SudokuNaive:
    def __init__(self,grid):
        self.grid = grid

    def find_empty(self):
        """
        Locates the next empty cell in the Sudoku grid.
        
        Args:
            self: the current SudokuNaive instance.
        
        Yields:
            A tuple representing the position of the next empty cell, or none if the
            puzzle is fully assigned.
        """
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] == 0:
                    return r, c
        return None
    
    def valid(self, num, row, col):
        """
        Docstring for valid
        
        Args:
            self: the current SudokuNaive instance.
            num: the candidate value to be tested between 1-9.
            row: the row index where the value is to be placed.
            col: the column index where the value is to be placed.

        Yields:
            True, if the placement is valid according to the rules of Sudoku. 
            Otherwise, returns false.
        """
        if num in self.grid[row]:
            return False

        for r in range(9):
            if self.grid[r][col] == num:
                return False

        br = (row // 3) * 3
        bc = (col // 3) * 3
        for r in range(br, br + 3):
            for c in range(bc, bc + 3):
                if self.grid[r][c] == num:
                    return False

        return True

    def solve(self):
        """
        Solve the Sudoku puzzle using the naive backtracking algorithm.
        
        Args:
            self: the current SudokuNaive instance.
        
        Yields:
            True, if the puzzle has been solved. Otherwise, returns false if no 
            solution could be found.
        """
        empty = self.find_empty()
        if not empty:
            return True

        row, col = empty

        for num in range(1, 10):
            if self.valid(num, row, col):
                self.grid[row][col] = num

                if self.solve():
                    return True

                self.grid[row][col] = 0

        return False

