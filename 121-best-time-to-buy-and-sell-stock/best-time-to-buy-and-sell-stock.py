class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mincost,maxprofit = float("inf"),float("-inf")
        for p in prices:
            mincost = min(mincost,p)
            maxprofit = max(maxprofit,p - mincost)
        return maxprofit