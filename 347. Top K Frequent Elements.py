class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        heap = []

        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))
        
        ans = []

        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
        
                
