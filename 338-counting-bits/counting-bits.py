class Solution:
    def countBits(self, n: int) -> List[int]:
        #Third Approach
        #n>>1 removes the lsb
        #n&1 returns 1 if last bit is 1 else 0
        #So in this dp approach we are using precomputed value of the number with one bit less than adding 1 or 0 depending if our number has 1 or 0 at the end
        dp = [0]* (n+1)
        for i in range(1,n+1):
            dp[i] = dp[i>>1]+ (i&1)
        return dp