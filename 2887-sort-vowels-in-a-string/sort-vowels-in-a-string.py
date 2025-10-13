from collections import deque
class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        vowels = {v: 0 for v in sorted("AEIOUaeiou")}
        vowelidx = []
        #find
        for i,l in enumerate(s):
            if l in vowels:
                vowels[l]+=1
                vowelidx.append(i)
        print(vowels)
        
        #update
        vowelidx = deque(vowelidx)
 
        for key in vowels:
            while vowels[key]>0:
                idx =vowelidx.popleft()
                s[idx] = key
                vowels[key]-=1


        s=''.join(s)
        return s



            