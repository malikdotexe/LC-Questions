import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #l is set to 1 instead of 0 as we dont want to try for 0 rate
        l = 1
        r = max(piles)
        ans= 0
        while l<=r:
            rate = l+(r-l)//2
            time = 0
            for b in piles:
                hours = math.ceil(b/rate)
                time+=hours
            
            #answer is valid but as we are optimizing for minimum rate we will shift to 
            #left side to try finding a slower valid rate
            if time<=h:
                ans = rate
                r = rate-1

            #answer is invalid so we will shift our rate to a higher side
            else:
                l = rate+1
        return ans
