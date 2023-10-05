class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge = self.merge(nums1, nums2)
        mid = len(merge) // 2
        if len(merge) % 2 == 0:
            return (float(merge[mid] + merge[mid - 1]) / 2)
        else:
            return merge[mid]
            
        
    def merge(self, nums1, nums2):
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        
        if i == len(nums1):
            result.extend(nums2[j:])
        else:
            result.extend(nums1[i:])
        return result

        
