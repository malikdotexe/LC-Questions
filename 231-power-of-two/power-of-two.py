class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        #number would be a power of 2 if it only has one bit set to 1 
        #So if we remove 1 from it and it becomes 0 return True
        if n==0:
            return False
        if n&(n-1)==0:
            return True
        return False