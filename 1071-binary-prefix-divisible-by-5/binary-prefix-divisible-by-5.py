class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        temp = 0
        res = []
        
        for bit in nums:
            temp = (temp * 2 + bit) % 5
            res.append(temp == 0)
        
        return res
