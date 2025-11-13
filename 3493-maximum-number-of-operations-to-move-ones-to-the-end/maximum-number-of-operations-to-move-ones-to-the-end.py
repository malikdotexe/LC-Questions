class Solution:
    def maxOperations(self, s: str) -> int:
        ones =0
        ans = 0
        for i,c in enumerate(s):
            if c=="1":
                ones+=1
            if c=="0" and i>0 and s[i-1]!="0":
                ans+=ones
        return ans
                    




