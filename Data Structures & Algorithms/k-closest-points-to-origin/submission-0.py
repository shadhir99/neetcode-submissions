class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        # return points[:k]

        heap = []

        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            heapq.heappush(heap, (distance, x, y))
        
        result = []
        while k > 0:
            distance, x, y = heapq.heappop(heap)
            result.append([x, y])
            k -= 1
        
        return result



        