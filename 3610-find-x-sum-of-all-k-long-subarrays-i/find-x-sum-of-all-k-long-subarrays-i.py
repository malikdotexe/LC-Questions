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
        
    def topKfrequent(self,nums,k):
        count = Counter(nums)
        countarr = [[y,x] for x,y in count.items()]
        heapq.heapify(countarr)
        while len(countarr)>k:
            heapq.heappop(countarr)
        res = [x[1] for x in countarr for _ in range(x[0])]
        return res