class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = [0] * len(matrix[0])

        rows = len(matrix)
        columns = len(matrix[0])

        hm = {}

        for i in range(rows):
            hm[i] = []
            for j in range(columns):
                if matrix[i][j] == 0:
                    hm[i].append(j)
        
        for key, value in hm.items():
            for col in value:
                for k in range(rows):
                    matrix[k][col] = 0

            if value:
                matrix[key] = zero_row
        
        
