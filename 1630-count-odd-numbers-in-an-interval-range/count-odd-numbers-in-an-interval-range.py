class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2 or high%2:
            return (high - low)//2+1
        else:
            return (high - low)//2
