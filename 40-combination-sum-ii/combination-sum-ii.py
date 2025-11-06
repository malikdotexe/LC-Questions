class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        candidates.sort()
        res = []
        def dfs(i,remaining):
            #cases
            #ideal case
            if remaining == 0:
                res.append(temp.copy())
                return
            #not ideal case
            if i==len(candidates) or remaining<0:
                return


            #choices
            #CHOICE 1 - Include the number
            temp.append(candidates[i])
            dfs(i+1,remaining - candidates[i])
            temp.pop() #backtrack

            #CHOICE 2 - Exclude the number 
            #As we dont want duplicates so like in threesum question we would skip our i pointer
            #till we find a unique value
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,remaining)

        
        dfs(0,target)
        return res
