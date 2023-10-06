class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        modifiable = []
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] == ".":
                    row.append(True)
                else:
                    row.append(False)
            modifiable.append(row)
        backtrack(0, board, modifiable)


def backtrack(index, board, modifiable):
    if (index == 81):
        return True

    row = index // 9
    column = index % 9

    for i in range(1, 10):
        # try the "i" valid value
        if modifiable[row][column]:
            board[row][column] = str(i)
            # if this i value is valid, proceed to the next cell
            # otherwise, it will try the next i value
            if isValid(row, column, board, str(i)) and backtrack(index + 1, board, modifiable):
                return True
        else:
            return backtrack(index + 1, board, modifiable)
    #
    board[row][column] = "."
    return False


def isValid(row, col, board, value):
    for i in range(9):
        if board[row][i] == value and i != col:
            return False
        if board[i][col] == value and i != row:
            return False
        square_row = 3 * (row // 3) + i // 3
        square_column = 3 * (col // 3) + i % 3
        if board[square_row][square_column] == value and (square_row != row and square_column != col):
            return False
    return True




