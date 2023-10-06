class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previousNum = None
        index = 0
        while index < len(nums):
            num = nums[index]
            if num == previousNum:
                nums.pop(index)
                index -= 1
            previousNum = num
            index += 1
