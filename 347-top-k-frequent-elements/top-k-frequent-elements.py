#with minheap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        countarr = [[y,x] for x,y in count.items()]
        heapq.heapify(countarr)
        while len(countarr)>k:
            heapq.heappop(countarr)
        res = [x[1] for x in countarr]
        return res