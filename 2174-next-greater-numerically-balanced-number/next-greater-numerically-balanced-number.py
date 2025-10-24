class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1,10000000):
            numstring = str(i)
            freqmap = Counter(numstring)
            if self.checker(freqmap):
                return i
    def checker(self,freqmap):
        for key,value in freqmap.items():
                if int(key)!=int(value):
                    return False            
        return True                    