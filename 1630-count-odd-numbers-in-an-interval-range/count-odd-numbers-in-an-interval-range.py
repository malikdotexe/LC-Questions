import math
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        lowodd = low%2 
        highodd = high%2
        if lowodd or highodd:
            return math.ceil((high - low)//2)+1
        else:
            return math.ceil(((high - low)//2))
