class Solution:
    def smallestNumber(self, n: int) -> int:
        power = 1
        while n>1:
            n=n//2
            power+=1
        return (2**power)-1


        