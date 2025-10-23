class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s=[int(x) for x in s]
        while len(s)>2:
            curr = []
            for i in range(0,len(s)-1):
                first = s[i]
                second = s[i+1]
                curr.append(((first+second)%10))
            s=curr
        return s[0]==s[1]