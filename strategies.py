import pandas as pd
from tests import box_rule, vertical_rule, horizontal_rule, check_rules
from box_finder import box_finder

def assign_starting_values(input_file):
    """
    Reads in the sudoku in csv format, converts into a list of lists (where the rows are the lists)
    """
    df = pd.read_csv(input_file)
    # Generates 9 rows
    gridline = []
    for i in range(9):
        gridline.append(0)
    # Generates 9x9 grid
    grid = []
    for i in range(9):
        grid.append(list(gridline))
    # Assigns the numbers from the csv to the grid
    for i in range(0,9):
        for j in range(0,9):
            grid[i][j] = df["col{}".format(j)][i]
    print("This is the starting board")
    print(*grid, sep="\n")
    print("")
    return(grid)

def only_possible_squares(x, grid):
    """
    Picks a box, loops through all squares looking to see if a number has to go in that square
    Picks next box, repeats
    """
    only_possible_squares_placed = False
    for col_def in [(0,1,2), (3,4,5), (6,7,8)]:
        for row_def in [(0,1,2), (3,4,5), (6,7,8)]:
            poss_posn = 0
            for i in col_def:
                for j in row_def:
                    if (grid[i][j] == 0):
                        m, n = box_finder(i, j)
                        allowed = check_rules(grid, x, i, j, m, n)
                        if allowed == 1:
                            poss_posn += 1
                            row = i
                            col = j
            if poss_posn == 1:
                grid[row][col] = x
                print("{} placed in position {}, {}".format(x, row, col))
                only_possible_squares_placed = True
            return grid, only_possible_squares_placed




def only_possible_number(grid, i, j, m, n):
    """
    Loops through all squares and checks to see if only 1 number is allowed
    """
    must = []
    only_possible_number_placed = False
    for x in range(1,10):
        if grid[i][j] == 0:
            allowed = check_rules(grid, x, i, j, m, n)
            if allowed == 1:
                must.append([x, [i,j]])
    if (len(must) == 1):
        row = must[0][1][0]
        col = must[0][1][1]
        grid[row][col] = must[0][0]
        print("{} placed in position {}, {}".format(must[0][0], row, col))
        only_possible_number_placed = True
    return grid, only_possible_number_placed
