class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mincost,maxprofit = float("inf"),float("-inf")
        for p in prices:
            mincost = min(p,mincost)
            profit = p - mincost 
            maxprofit = max(profit,maxprofit)
        return maxprofit