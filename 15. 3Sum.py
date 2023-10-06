class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums = sorted(nums)
        ans = set()

        for i in range(n):
            j = i + 1
            k = n - 1

            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]

                if sum_ == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum_ < 0:
                    j += 1
                else:
                    k -= 1


        return list(ans)
