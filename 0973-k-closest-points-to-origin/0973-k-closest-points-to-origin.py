class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            curr_dist =- ((point[0]*point[0]) + (point[1]*point[1]))
            heapq.heappush(heap,[curr_dist,point])
            curr_dist = 0
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for dist , point in heap:
            res.append(point)
        return res
        
        
        

        