class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap and hashMap[complement] != i:
                return [i, hashMap[complement]]
            else:
                hashMap[nums[i]] = i
        
        return []
