class SudokuCSP:
    def __init__(self, grid):
        self.grid = grid
        self.domains = {
            (r,c): self.get_domain(r,c) if grid[r][c] == 0 else {grid[r][c]}
            for r in range(9)
            for c in range(9)
        }

    def get_domain(self, row, col):
        """
        Determines which values between 1-9 can be placed in the specified cell 
        without violating Sudoku constraints.

        Args:
            row: the row index of the cell.
            col: the column index of the cell.

        Yields:
            The legal values for the cell.
        """
        if self.grid[row][col] != 0:
            return {self.grid[row][col]}

        used = set()

        used.update(self.grid[row])

        used.update(self.grid[r][col] for r in range(9))

        br = (row // 3) * 3
        bc = (col // 3) * 3
        for r in range(br, br + 3):
            for c in range(bc, bc + 3):
                used.add(self.grid[r][c])

        return {n for n in range(1, 10) if n not in used}

    def select_unassigned_variable(self):
        """
        Select the next variable using the MRV algorithm.

        Args:
            self: The current SudokuCSP instance.

        Yields:
            A tuple representing the most constrained unassigned cell.
        """
        unassigned = [
            (cell, dom) for cell, dom in self.domains.items()
            if self.grid[cell[0]][cell[1]] == 0
        ]

        cell, _ = min(unassigned, key=lambda x: len(x[1]))
        return cell

    def order_domain_values(self, cell):
        """
        Order domain values using the LCV algorithm.

        Args:
            cell: the variable being assigned.

        Yields:
            A list of domain values sorted from least to most constraining.
        """
        row, col = cell

        def count_constraints(value):
            count = 0
            for r in range(9):
                for c in range(9):
                    if (r, c) != cell and self.grid[r][c] == 0:
                        if value in self.get_domain(r, c):
                            if r == row or c == col or (r // 3 == row // 3 and c 
                                                        // 3 == col // 3):
                                count += 1
            return count

        domain = list(self.domains[cell])
        return sorted(domain, key=count_constraints)

    def forward_check(self, cell, value):
        """
        Applies forward checking after assigning a value to a specific cell.

        Args:
            cell: the variable being assigned.
            value: the value being assigned to the cell.

        Yields:
            A list of domain removals for later. Otherwise, return None if a failure
            occurs.
        """
        row, col = cell
        removed = []

        for r in range(9):
            for c in range(9):
                if (r, c) != cell and self.grid[r][c] == 0:
                    if r == row or c == col or (r // 3 == row // 3 and c // 3 == col // 3):
                        if value in self.domains[(r, c)]:
                            self.domains[(r, c)].remove(value)
                            removed.append(((r, c), value))

                            if len(self.domains[(r, c)]) == 0:
                                for (rr, cc), val in removed:
                                    self.domains[(rr, cc)].add(val)
                                return None

        return removed

    def solve(self):
        """
        Solve the Sudoku puzzle using smart CSP algorithms.

        Args:
            self: the current SudokuCSP instance.

        Yields:
            True, if the puzzle is solved successfully. Otherwise, returns false.
        """
        if all(self.grid[r][c] != 0 for r in range(9) for c in range(9)):
            return True

        cell = self.select_unassigned_variable()
        row, col = cell

        for value in self.order_domain_values(cell):
            self.grid[row][col] = value
            old_domain = self.domains[cell]
            self.domains[cell] = {value}

            removed = self.forward_check(cell, value)
            if removed is not None:
                if self.solve():
                    return True

                for (r, c), val in removed:
                    self.domains[(r, c)].add(val)

            self.grid[row][col] = 0
            self.domains[cell] = old_domain

        return False