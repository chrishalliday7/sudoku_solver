from strategies import only_possible_squares, only_possible_number, assign_starting_values
from box_finder import box_finder
import time

# Show computation time
start_time = time.time()

grid = assign_starting_values("input_medium.csv")

def solve(grid):
    """
    Begins the solver, using 2 strategies
    Only possible squares: looks for squares that are the only place in a row/column/box that a number can go
    Only possible numbers: selects a box and loops through all numbers to see if there exists only 1 number that fits
    i = row number
    j = column number
    """
    print("")
    print("Only Possible Squares")
    for i in range(0,9):
        for j in range(0,9):
            for x in range(1,10):
                grid = only_possible_squares(x, grid)

    print("")
    print("Only Possible Numbers")
    for i in range(0,9):
        for j in range(0,9):
            m, n = box_finder(i, j)
            only_possible_number(grid, i, j, m, n)
    return grid

# Loops through the solver until all squares are filled
for i in range(0,9):
    for j in range(0,9):
        if grid[i][j] == 0:
            solve(grid)

print("")
print("Solved Sudoku")
print(*grid, sep="\n")
print ("")
print("--- %s seconds ---" % (time.time() - start_time))


"""
Add logic for "candidate" numbers
"""