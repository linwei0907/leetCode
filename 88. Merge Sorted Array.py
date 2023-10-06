class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        heap = []

        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                heapq.heappush(heap, nums1[i])
                i += 1
            else:
                heapq.heappush(heap, nums2[j])
                j += 1

        while i < m:
            heapq.heappush(heap, nums1[i])
            i += 1
        
        while j < n:
            heapq.heappush(heap, nums2[j])
            j += 1
        
        for i in range(len(nums1)):
            nums1[i] = heapq.heappop(heap)
        
