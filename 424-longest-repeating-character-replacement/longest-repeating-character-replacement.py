from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l= 0
        Count = defaultdict(int)
        maxlen = 0

        for r in range(len(s)):
            Count[s[r]] +=1
            #We will shrink from left till we get a valid string
            while (r-l+1)-max(Count.values())>k :
                Count[s[l]]-=1
                l+=1
            #update maxlen if current valid string length is bigger
            maxlen = max(maxlen,r-l+1)
        return maxlen
                

                

