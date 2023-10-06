class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        threshold = len(nums) // 3

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        res = []

        for key, value in freq.items():
            if value > threshold:
                res.append(key)

        return res
