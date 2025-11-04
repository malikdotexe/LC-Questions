class Solution:
    def countBits(self, n: int) -> List[int]:
        # First solution formula 1+dp[n-offset]
        # We use the precomputed result for the difference between n and the largest power of 2 less than or equal to n, then add 1 for the new set bit introduced by that power of 2.
        # n-binary-numberofones
        # 0-00-0   
        # 1-01-1    1+dp[1-1] 
        # 2-10-1    1+dp[2-2] new offset 
        # 3-11-2    1+dp[3-2]
        # 4-100-1   1+dp[4-4] new offset
        # 5-101-2   1+dp[5-4] computing new range(4-8) using previous range(0-4) and just addin 1  
        # 6-110-2   1+dp[6-4]
        # 7-111-3   1+dp[7-4]
        # 8-1000-1  1+dp[8-8] computing new range(8-16) using previous range(0-8) and just addin 1
        dp = [0]*(n+1)
        offset = 1
        for i in range(1,n+1):
            if offset*2==i:
                offset = i
            dp[i]= 1+dp[i-offset]
        return dp