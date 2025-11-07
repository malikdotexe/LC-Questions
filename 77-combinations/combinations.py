class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp = []
        res = []
        num = [x for x in range(1,n+1)]
        def dfs(i):
            #base
            if len(temp)==k:
                res.append(temp.copy())
                return
            if i == n:
                return
            #choices
            # choice 1
            temp.append(num[i]) 
            dfs(i+1)

            temp.pop() #backtrack
            #choice 2
            dfs(i+1)
        dfs(0)
        return res
