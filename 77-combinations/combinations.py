class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp = []
        res = []
        def dfs(start):
            if len(temp)==k:
                res.append(temp.copy())
            for i in range(start,n+1):
                temp.append(i)
                dfs(i+1)
                temp.pop()

        dfs(1)
        return res
