class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calcPow(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            if not n%2: #even power
                return calcPow(x*x,n//2)
            elif n%2: #odd power
                return x*calcPow(x*x,n//2)
        if n>=0:
            return calcPow(x,n)
        else:
            return 1/calcPow(x,abs(n))