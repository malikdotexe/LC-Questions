class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
    
        for i in range(len(prices)):
            if i<len(prices)-1 and prices[i+1]>prices[i]:
                res+= prices[i+1]-prices[i]
        return res


