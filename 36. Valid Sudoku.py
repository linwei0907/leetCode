class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = 9
        column = 9

        for row in range(len(board)):
            nums_in_row = []
            for column in range(len(board)):
                if board[row][column] != ".":
                    if board[row][column] in nums_in_row:
                        return False
                    else:
                        nums_in_row.append(board[row][column])
        
        for column in range(len(board)):
            nums_in_column = []
            for row in range(len(board)):
                if board[row][column] != ".":
                    if board[row][column] in nums_in_column:
                        return False
                    else:
                        nums_in_column.append(board[row][column])

        sub_boxes = [
            ([0,1,2], [0,1,2]),([0,1,2], [3,4,5]),([0,1,2],[6,7,8]),
            ([3,4,5], [0,1,2]),([3,4,5], [3,4,5]),([3,4,5],[6,7,8]),
            ([6,7,8], [0,1,2]),([6,7,8], [3,4,5]),([6,7,8],[6,7,8]),
            ]

        for box in sub_boxes:
            numbers_in_box = []
            for row in box[0]:
                for column in box[1]:
                    if board[row][column] != ".":
                        if board[row][column] in numbers_in_box:
                            return False
                        else:
                            numbers_in_box.append(board[row][column])


        
        return True
