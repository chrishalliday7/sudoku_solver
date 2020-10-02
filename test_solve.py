from strategies import assign_starting_values
from sudoku import solve

def test_easy():
    """
    Easy #215
    """
    solution = [
        [8,9,1,4,7,3,6,2,5],
        [2,3,5,9,1,6,7,4,8],
        [6,4,7,5,8,2,3,9,1],
        [9,1,3,7,6,8,4,5,2],
        [5,6,2,3,4,1,8,7,9],
        [7,8,4,2,9,5,1,3,6],
        [1,7,9,6,5,4,2,8,3],
        [3,5,8,1,2,7,9,6,4],
        [4,2,6,8,3,9,5,1,7]
    ]
    grid = assign_starting_values("input_easy.csv")
    solved_grid = solve(grid)

    assert len(solution) ==  len(solved_grid)
    assert solution == solved_grid

def test_medium():
    """
    Medium #264
    """
    solution = [
        [5,8,7,9,2,3,4,6,1],
        [1,4,3,8,5,6,7,2,9],
        [2,6,9,1,4,7,5,3,8],
        [9,5,6,4,7,2,8,1,3],
        [4,2,1,3,9,8,6,7,5],
        [3,7,8,6,1,5,2,9,4],
        [6,3,2,5,8,1,9,4,7],
        [7,9,5,2,3,4,1,8,6],
        [8,1,4,7,6,9,3,5,2]
    ]
    grid = assign_starting_values("input_medium.csv")
    solved_grid = solve(grid)

    assert len(solution) ==  len(solved_grid)
    assert solution == solved_grid

def test_hard():
    """
    Hard #295
    """
    solution = [
        [8,2,1,6,5,4,3,9,7],
        [5,9,4,7,3,8,1,2,6],
        [6,7,3,1,2,9,4,8,5],
        [7,5,6,3,8,2,9,4,1],
        [4,1,8,9,6,7,2,5,3],
        [9,3,2,4,1,5,6,7,8],
        [2,6,9,5,7,1,8,3,4],
        [1,8,7,2,4,3,5,6,9],
        [3,4,5,8,9,6,7,1,2]
    ]
    grid = assign_starting_values("input_hard.csv")
    solved_grid = solve(grid)

    assert len(solution) ==  len(solved_grid)
    assert solution == solved_grid