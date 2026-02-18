from naive_backtracking import SudokuNaive
from smart_backtracking import SudokuCSP
import time

def load_sudoku_from_file(path):
    """
    Load a Sudoku puzzle from a text file.

    Args:
        path: the file path to the Sudoku puzzle.

    Yields:
        A 9x9 list of lists containing integers representing the puzzle grid.
    """
    with open(path, "r") as f:
        lines = f.readlines()

    grid = []
    for line in lines:
        line = line.strip()
        if len(line) == 9 and line.isdigit():
            grid.append([int(ch) for ch in line])

    return grid

def print_grid(grid):
    """
    Display the Sudoku grid in the correct format.

    Args:
        grid: a 9x9 list of lists representing the Sudoku puzzle.

    Yields:
        A printed grid on the console.
    """
    for row in grid:
        print(" ".join(str(n) if n != 0 else "." for n in row))
    print()

def run_solvers(grid, mode = "naive"):
    """
    Execute the selected Sudoku solver on a given puzzle.

    Args:
        grid: a 9x9 list of lists representing the Sudoku puzzle.
        mode: which solver to use, either naive or smart backtracking algorithms.

    Yields:
        A printed solution and how long it took to solve the puzzle.
    """
    if mode == "naive":
        solver = SudokuNaive(grid)
    else:
        solver = SudokuCSP(grid)

    print(f"Running {mode.upper()} solver...")
    start = time.time()
    solved = solver.solve()
    end = time.time()

    if solved:
        print("Solved Sudoku:")
        print_grid(solver.grid)
        print(f"Time: {end - start:.4f} seconds")
    else:
        print("No solution found.")

if __name__ == "__main__":
    path = input("Enter the file path to your Sudoku puzzle: ")
    mode = input("Choose solver (naive or smart): ").strip().lower()

    grid = load_sudoku_from_file(path)
    print("Initial Puzzle: ")
    print_grid(grid)

    run_solvers(grid, mode)