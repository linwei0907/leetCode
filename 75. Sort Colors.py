class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j ,k = 0 , 0, len(nums) - 1

        while j <= k:
            if nums[j] == 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                temp = nums[k]
                nums[k] = nums[j]
                nums[j] = temp
                k -= 1


        
