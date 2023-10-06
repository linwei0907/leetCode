class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[0])):
                row.append(False)
            visited.append(row)

        visits = 1
        elements = len(matrix) * len(matrix[0])

        res = [matrix[0][0]]
        row = 0
        column = 0
        visited[0][0] = True
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0
        
        while visits < elements:
            row_ = row + direction[curr_dir][0]
            column_ = column + direction[curr_dir][1]
            if  0 <= row_ < len(matrix) and 0 <= column_ < len(matrix[0]) and not visited[row_][column_]:
                row = row_
                column = column_
                visited[row][column] = True
                visits += 1
                res.append(matrix[row][column])
            else:
                curr_dir = (curr_dir + 1) % len(direction)
            print(res, visits)

        return res
