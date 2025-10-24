import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            #negating the - we did in the start to maxheapify
            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)
            if x!=y:
                heapq.heappush(maxheap,y-x)
        
        return abs(maxheap[0]) if maxheap else 0