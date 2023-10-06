class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid_ = (start + end) // 2
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > nums[-1]:
                start = mid + 1
            else:
                end = mid - 1
        
        left_end = self.b_search(0, end, nums, target)
        if left_end != -1:
            return left_end
        
        return self.b_search(end + 1, len(nums) - 1, nums, target)


    def b_search(self, start, end, nums, target):
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        
        return -1
