class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        result = []

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                j += 1
                i += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
        
        return result
