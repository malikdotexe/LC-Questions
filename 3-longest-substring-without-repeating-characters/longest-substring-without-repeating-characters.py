from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
   
        #sliding window approach, here we initialize a Count hashmap to store the frequency of letters, if after including a letter , its frequency goes above 1 we need to keep shrinking our string from left (while reducing the frequency of the letter which is getting excluded) till it comes back to 1. And at each step we update the maxlen(r-l+1)
        l = 0
        maxlen = 0
        Count = defaultdict(int)
        for r in range(len(s)):
            Count[s[r]] +=1
            while Count[s[r]]>1:
                Count[s[l]]-=1
                l+=1
            currlen = (r-l)+1
            maxlen= max(maxlen,currlen)
        return maxlen
            
