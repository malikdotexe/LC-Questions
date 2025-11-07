class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []
        def dfs(closen,openn):
            #base
            if len(temp)==(2*n):
                res.append("".join(temp))
                return
            #choices
            
            if openn<n:
                temp.append('(')#to open another bracket
                dfs(closen,openn+1)
                temp.pop()
            if closen<openn:    
                temp.append(')')#to add closing bracket
                dfs(closen+1,openn)
                temp.pop()
            


        dfs(0,0)
        return res
            