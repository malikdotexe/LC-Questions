class Solution:
    def countBits(self, n: int) -> List[int]:
        #Second approach
        #for even numbers ,number of set bits(1) are same as that of the number//2
        #Eg - 14 has same set bits as 7 
        #for odd nums, its same as the set bits of (number//2) + 1
        #Eg - 7 has same set bits as (7/2 = 3) + 1 => 3 has 2 set bits ,adding 1 gives us 3
        dp = [0]*(n+1)
        for i in range(1,n+1):
            #even
            if i%2==0:
                dp[i]=dp[i//2]
            #odd 
            elif i%2!=0:
                dp[i]=dp[i//2]+1
        return dp
