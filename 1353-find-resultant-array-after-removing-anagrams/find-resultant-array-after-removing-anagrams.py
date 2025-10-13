class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:    
        #counter array
        countn = [0]*26
        for l in words[0]:
            countn[ord(l)-ord('a')]+=1
        stack = [countn]
        res=[words[0]]
        for word in words:
            countn = [0]*26
            for l in word:
                countn[ord(l)-ord('a')]+=1
            if stack[-1] != countn:
                stack.append(countn)
                res.append(word)
        return res
