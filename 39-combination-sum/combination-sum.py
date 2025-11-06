class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp =[]

        def dfs(i,remaining):
            #base
            if i==len(candidates) or remaining<0:
                return
            if remaining == 0:
                res.append(temp.copy())
                return
            #choices
            temp.append(candidates[i])
            dfs(i,remaining-candidates[i]) #continue with number included
            temp.pop() #backtrack
            dfs(i+1,remaining) #continue with number excluded
        dfs(0,target)
        return res