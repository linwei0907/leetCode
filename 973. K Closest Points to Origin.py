class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            distance = self.calc_distance(points[i][0], points[i][1])
            heapq.heappush(heap, (distance, points[i]))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result


    
    def calc_distance(self, x, y):
        return ((x - 0) ** 2 + (y - 0) ** 2) ** .5
