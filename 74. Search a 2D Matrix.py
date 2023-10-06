class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            num = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if num == target:
                return True
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
