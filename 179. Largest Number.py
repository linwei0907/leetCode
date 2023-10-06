class Solution(object):    
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        result = self.mergeSort(0, len(nums) - 1, nums)
        for i in range(len(result)):
            result[i] = str(result[i])
        return str(int("".join(result)))

    def mergeSort(self, l, r, nums):
        if l > r:
            return
        if l == r:
            return [nums[l]]
        mid = l + (r - l) // 2

        left = self.mergeSort(l, mid, nums)
        right = self.mergeSort(mid + 1, r, nums)

        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if self.compare(str(left[i]), str(right[j])):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        if i == len(left):
            result.extend(right[j:])
        else:
            result.extend(left[i:])

        return result

    def compare(self, str1, str2):
        if str1 + str2 > str2 + str1:
            return True
        return False
