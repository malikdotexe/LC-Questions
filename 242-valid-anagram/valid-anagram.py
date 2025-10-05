class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 =[0]*26
        count2 =[0]*26
        for c in s:
            idx = ord(c)-ord("a")
            count1[idx]+=1
        for c in t:
            
            idx = ord(c)-ord("a")
            count2[idx]+=1
        return count1==count2
