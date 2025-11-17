class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        gap = k
        for n in nums:
            if n == 1:
                if gap < k:
                    return False
                gap = 0
            else:
                gap += 1 
        return True

            