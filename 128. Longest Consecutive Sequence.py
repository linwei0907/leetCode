class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = num + 1
        

        sequence = []
        max_length = 0
        for key, value in hashMap.items():
            if key - 1 not in hashMap:
                sequence.append(key)
                while value in hashMap:
                    sequence.append(value)
                    value = hashMap[value]
                if len(sequence) > max_length:
                    max_length = len(sequence)

                sequence = []
        
        return max_length
