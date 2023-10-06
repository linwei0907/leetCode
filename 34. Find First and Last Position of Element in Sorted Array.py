class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        end = len(nums) - 1
        start = 0
        res = [-1, -1]
        found = False
        while start <= end:
            index = (start + end) // 2
            if nums[index] < target:
                start = index + 1
            elif nums[index] > target:
                end = index - 1
            else:
                found = True
                end -= 1
        
        if not found:
            return res
        res[0] = start
        end = len(nums) - 1

        while start <= end:
            index = (start + end) // 2
            if nums[index] < target:
                start = index + 1
            elif nums[index] > target:
                end = index - 1
            else:
                start += 1

        res[1] = end
        return res
