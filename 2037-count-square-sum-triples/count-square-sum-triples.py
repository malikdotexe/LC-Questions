import math
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1,n):
            for b in range(1,n):
                c = math.sqrt(a**2+b**2)
                if c<=n and c%1==0:
                    count+=1
        return count