class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = 0 
        maxsum= float("-inf")
        for num in nums:
            currsum += num
            maxsum = max(maxsum,currsum)
            if currsum<0:
                currsum = 0
        return maxsum
