import heapq
class KthLargest:
    #Our approach is we would create a min heap of only k length and kth largest element would be the top of this min heap as lets say k = 3 => we would keep popping from top of our min heap till our length becomes k this would leave us biggest 3 numbers as small numbers are getting pop each time leaving larger numbers and finall y kth largest of these would be the element at the top(min of the heap)
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap)>k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)