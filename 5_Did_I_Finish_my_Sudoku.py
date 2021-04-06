# Description:
# Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter. If the board is valid return
# 'Finished!', otherwise return 'Try again!'
#
# Sudoku rules:

#
# Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only
# once.
#
# Rows:
#
#
# There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9.
# There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.
#
# In the illustration the numbers 5, 3, 1, and 2 are the "givens". They can not be changed. The remaining numbers in
# black are the numbers that you fill in to complete the row.
#
# Columns:
#
#
# There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the
# numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Again, there may not be any duplicate numbers in any column. Each column will
# be unique as a result.
#
# In the illustration the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining
# numbers as shown in black to complete the column.
#
# Regions
#
#
# A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.
#
# Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8,
# and 9. Duplicate numbers are not permitted in any region. Each region will differ from the other regions.
#
# In the illustration the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers
# as shown in black to complete the region.
#
# Valid board example:
#
#
# For those who don't know the game, here are some information about rules and how to play Sudoku:
# http://en.wikipedia.org/wiki/Sudoku and http://www.sudokuessentials.com/


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