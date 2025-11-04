import heapq
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i+k-1>len(nums)-1:
                break
            curr = nums[i:i+k]
            temp = self.topKfrequent(curr,x)
            print(f"curr - {curr} and temp is {temp}")
            res.append(sum(temp))
        return res
        
    def topKfrequent(self, nums, k):
        count = Counter(nums)
        # max heap
        heap = [(-freq, -num) for num, freq in count.items()]
        heapq.heapify(heap)

        res = []
        for _ in range(min(k, len(heap))):
            freq, num = heapq.heappop(heap)
            # negating by * with -1
            res.append((-freq) * (-num))
        return res