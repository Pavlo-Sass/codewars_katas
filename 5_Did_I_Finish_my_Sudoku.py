

def is_true(cell):
    # if all number in cell is various and all of them is < 9 than is Ok
    for i in cell:
        if int(i) > 9:
            return False
    return len(set(cell)) == 9


def done_or_not(board):
    # checking 3 x 3 cell for done
    # dividing 9x9 field on 3x3 cells
    for i in range(3, 10, 3):
        for j in range(3, 10, 3):
            cell = []
            for n in range(i-3, i):
                for m in range(j-3, j):
                    # checking is ok
                    cell.append(board[n][m])
            if not is_true(cell):
                return 'Try again!'

    for i in range(9):
        # checking horizontal line
        if not is_true(board[i]):
            return 'Try again!'
        cell = []
        for j in range(9):
            # checking vertical line
            cell.append(board[j][i])
        if not is_true(cell):
            return 'Try again!'
    return 'Finished!'


a = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
    ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
    ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
    ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
    ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
    ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
    ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
    ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
    ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]

print(done_or_not(a))