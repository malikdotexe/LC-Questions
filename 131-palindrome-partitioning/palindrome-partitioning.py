class Solution:
    def partition(self, s: str) -> List[List[str]]:
        temp = []
        res = []
        def backtrack(i):
            #base case
            if i>=len(s):
                res.append(temp.copy())
                return
            
            for j in range(i,len(s)):
                if self.isPal(s,i,j):
                    temp.append(s[i:j+1])
                    backtrack(j+1)
                    temp.pop()
        backtrack(0)
        return res

    def isPal(self,s,i,j):
        l,r = i,j
        while l<r:
            if s[l]!=s[r]:
                return False
            l,r=l+1,r-1
        return True