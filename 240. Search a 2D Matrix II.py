class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            find = self.search(row, target)
            if find != -1:
                return True
        
        return False
    
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
