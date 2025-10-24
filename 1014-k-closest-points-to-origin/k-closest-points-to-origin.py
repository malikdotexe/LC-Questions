import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist= (point[0])**2 + (point[1])**2
            heap.append([dist,point[0],point[1]])
        heapq.heapify(heap)
        res = []
        while len(res)!=k:
            point = heapq.heappop(heap)
            res.append([point[1],point[2]])
        return res