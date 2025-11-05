class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        maxpal = s[0]
        for i in range(len(s)):
            #even length
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                pal = s[l:r+1]
                if len(pal)>len(maxpal):
                    maxpal=pal
                l-=1
                r+=1
            #odd length
            l,r=i-1,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                pal = s[l:r+1]
                if len(pal)>len(maxpal):
                    maxpal=pal
                l-=1
                r+=1
        return maxpal