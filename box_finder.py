def box_finder(i, j):
    """
    Each box is defined by its row, column indices
    Takes i, j location of square of interest
    Returns m and n which represent the rows/columns to loop through for a particular box
    """
    boxes = [[(0,3), (0,3)], [(0,3), (3,6)], [(0,3), (6,9)],
             [(3,6), (0,3)], [(3,6), (3,6)], [(3,6), (6,9)],
             [(6,9), (0,3)], [(6,9), (3,6)], [(6,9), (6,9)]
            ]
    if i == 0:
        if j == 0:
            m = boxes[0][0][1]
            n = boxes[0][1][1]
        elif j == 1:
            m = boxes[0][0][1]
            n = boxes[0][1][1]
        elif j == 2:
            m = boxes[0][0][1]
            n = boxes[0][1][1]
        elif j == 3:
            m = boxes[1][0][1]
            n = boxes[1][1][1]
        elif j == 4:
            m = boxes[1][0][1]
            n = boxes[1][1][1]
        elif j == 5:
            m = boxes[1][0][1]
            n = boxes[1][1][1]
        elif j == 6:
            m = boxes[2][0][1]
            n = boxes[2][1][1]
        elif j == 7:
            m = boxes[2][0][1]
            n = boxes[2][1][1]
        elif j == 8:
            m = boxes[2][0][1]
            n = boxes[2][1][1]
    elif i == 1:
        if j == 0:
            m = boxes[0][0][1]
            n = boxes[0][1][1]
        elif j == 1:
            m = boxes[0][0][1]
            n = boxes[0][1][1]
        elif j == 2:
            m = boxes[0][0][1]
            n = boxes[0][1][1]
        elif j == 3:
            m = boxes[1][0][1]
            n = boxes[1][1][1]
        elif j == 4:
            m = boxes[1][0][1]
            n = boxes[1][1][1]
        elif j == 5:
            m = boxes[1][0][1]
            n = boxes[1][1][1]
        elif j == 6:
            m = boxes[2][0][1]
            n = boxes[2][1][1]
        elif j == 7:
            m = boxes[2][0][1]
            n = boxes[2][1][1]
        elif j == 8:
            m = boxes[2][0][1]
            n = boxes[2][1][1]
    elif i == 2:
        if j == 0:
            m = boxes[0][0][1]
            n = boxes[0][1][1]
        elif j == 1:
            m = boxes[0][0][1]
            n = boxes[0][1][1]
        elif j == 2:
            m = boxes[0][0][1]
            n = boxes[0][1][1]
        elif j == 3:
            m = boxes[1][0][1]
            n = boxes[1][1][1]
        elif j == 4:
            m = boxes[1][0][1]
            n = boxes[1][1][1]
        elif j == 5:
            m = boxes[1][0][1]
            n = boxes[1][1][1]
        elif j == 6:
            m = boxes[2][0][1]
            n = boxes[2][1][1]
        elif j == 7:
            m = boxes[2][0][1]
            n = boxes[2][1][1]
        elif j == 8:
            m = boxes[2][0][1]
            n = boxes[2][1][1]
    elif i == 3:
        if j == 0:
            m = boxes[3][0][1]
            n = boxes[3][1][1]
        elif j == 1:
            m = boxes[3][0][1]
            n = boxes[3][1][1]
        elif j == 2:
            m = boxes[3][0][1]
            n = boxes[3][1][1]
        elif j == 3:
            m = boxes[4][0][1]
            n = boxes[4][1][1]
        elif j == 4:
            m = boxes[4][0][1]
            n = boxes[4][1][1]
        elif j == 5:
            m = boxes[4][0][1]
            n = boxes[4][1][1]
        elif j == 6:
            m = boxes[5][0][1]
            n = boxes[5][1][1]
        elif j == 7:
            m = boxes[5][0][1]
            n = boxes[5][1][1]
        elif j == 8:
            m = boxes[5][0][1]
            n = boxes[5][1][1]
    elif i == 4:
        if j == 0:
            m = boxes[3][0][1]
            n = boxes[3][1][1]
        elif j == 1:
            m = boxes[3][0][1]
            n = boxes[3][1][1]
        elif j == 2:
            m = boxes[3][0][1]
            n = boxes[3][1][1]
        elif j == 3:
            m = boxes[4][0][1]
            n = boxes[4][1][1]
        elif j == 4:
            m = boxes[4][0][1]
            n = boxes[4][1][1]
        elif j == 5:
            m = boxes[4][0][1]
            n = boxes[4][1][1]
        elif j == 6:
            m = boxes[5][0][1]
            n = boxes[5][1][1]
        elif j == 7:
            m = boxes[5][0][1]
            n = boxes[5][1][1]
        elif j == 8:
            m = boxes[5][0][1]
            n = boxes[5][1][1]
    elif i == 5:
        if j == 0:
            m = boxes[3][0][1]
            n = boxes[3][1][1]
        elif j == 1:
            m = boxes[3][0][1]
            n = boxes[3][1][1]
        elif j == 2:
            m = boxes[3][0][1]
            n = boxes[3][1][1]
        elif j == 3:
            m = boxes[4][0][1]
            n = boxes[4][1][1]
        elif j == 4:
            m = boxes[4][0][1]
            n = boxes[4][1][1]
        elif j == 5:
            m = boxes[4][0][1]
            n = boxes[4][1][1]
        elif j == 6:
            m = boxes[5][0][1]
            n = boxes[5][1][1]
        elif j == 7:
            m = boxes[5][0][1]
            n = boxes[5][1][1]
        elif j == 8:
            m = boxes[5][0][1]
            n = boxes[5][1][1]
    elif i == 6:
        if j == 0:
            m = boxes[6][0][1]
            n = boxes[6][1][1]
        elif j == 1:
            m = boxes[6][0][1]
            n = boxes[6][1][1]
        elif j == 2:
            m = boxes[6][0][1]
            n = boxes[6][1][1]
        elif j == 3:
            m = boxes[7][0][1]
            n = boxes[7][1][1]
        elif j == 4:
            m = boxes[7][0][1]
            n = boxes[7][1][1]
        elif j == 5:
            m = boxes[7][0][1]
            n = boxes[7][1][1]
        elif j == 6:
            m = boxes[8][0][1]
            n = boxes[8][1][1]
        elif j == 7:
            m = boxes[8][0][1]
            n = boxes[8][1][1]
        elif j == 8:
            m = boxes[8][0][1]
            n = boxes[8][1][1]
    elif i == 7:
        if j == 0:
            m = boxes[6][0][1]
            n = boxes[6][1][1]
        elif j == 1:
            m = boxes[6][0][1]
            n = boxes[6][1][1]
        elif j == 2:
            m = boxes[6][0][1]
            n = boxes[6][1][1]
        elif j == 3:
            m = boxes[7][0][1]
            n = boxes[7][1][1]
        elif j == 4:
            m = boxes[7][0][1]
            n = boxes[7][1][1]
        elif j == 5:
            m = boxes[7][0][1]
            n = boxes[7][1][1]
        elif j == 6:
            m = boxes[8][0][1]
            n = boxes[8][1][1]
        elif j == 7:
            m = boxes[8][0][1]
            n = boxes[8][1][1]
        elif j == 8:
            m = boxes[8][0][1]
            n = boxes[8][1][1]
    elif i == 8:
        if j == 0:
            m = boxes[6][0][1]
            n = boxes[6][1][1]
        elif j == 1:
            m = boxes[6][0][1]
            n = boxes[6][1][1]
        elif j == 2:
            m = boxes[6][0][1]
            n = boxes[6][1][1]
        elif j == 3:
            m = boxes[7][0][1]
            n = boxes[7][1][1]
        elif j == 4:
            m = boxes[7][0][1]
            n = boxes[7][1][1]
        elif j == 5:
            m = boxes[7][0][1]
            n = boxes[7][1][1]
        elif j == 6:
            m = boxes[8][0][1]
            n = boxes[8][1][1]
        elif j == 7:
            m = boxes[8][0][1]
            n = boxes[8][1][1]
        elif j == 8:
            m = boxes[8][0][1]
            n = boxes[8][1][1]
    return m, n