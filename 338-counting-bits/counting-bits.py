class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self.countones(i))
        return res

    def countones(self,n):
        res = 0 
        while n:
            n = n&(n-1)
            res+=1
        return res