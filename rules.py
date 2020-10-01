def box_rule(grid, x, m, n):
    """
    Takes all numbers in a particular box and puts them into a list
    Checks existence of selected number
    """
    box = []
    for row in range(m-3, m):
        for col in range(n-3,n):
            box.append(grid[row][col])
    if x in box:
        return False
    else:
        return True        

def horizontal_rule(grid, x, i):
    """
    Checks if number is in a particular row (list)
    """
    if x in grid[i]: 
        return False
    else:
        return True

def vertical_rule(grid, x, i, j):
    """
    Assigns the nth entry of each row into a new list to represent the nth column
    Checks if selected number is in that list
    """
    column = []
    for n in range(0,9):
        column.append(grid[n][j])
    if x in column:
        return False
    else:
        return True

def check_rules(grid, x, i, j, m ,n):
    """
    Checks whether selected number can go in particular square
    """
    HR = horizontal_rule(grid, x, i)
    VR = vertical_rule(grid, x, i, j)
    BR = box_rule(grid, x, m, n)
    if HR and VR and BR:
        allowed = 1
    else:
        allowed = 0
    return allowed


