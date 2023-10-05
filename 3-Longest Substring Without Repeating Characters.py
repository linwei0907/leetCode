class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        hashMap = {}
        max_len = 0
        for char in s:
            if char in hashMap and hashMap[char] >= left:
                left = hashMap[char] + 1
            else:
                max_len = max(right - left + 1, max_len)
            hashMap[char] = right
            right += 1
        
        return max_len
