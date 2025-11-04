class Solution:
    def hammingWeight(self, n: int) -> int:
        #Second Solution
        #If we AND n with n-1 we can remove 1 , and the number of times we can do that would be our answer
        res = 0
        while n!=0:
            n = n&(n-1)
            res+=1
        return res
        
        
        
        #First solution
        #modding by 2 returns 1 if last bit is 1 else 0 , and then we right shift by 1 (>>1) to do the operation on new bit until there are no bits left
        # res = 0 
        # while n!=0:
        #     res += n%2
        #     n = n>>1
        # return res
        

