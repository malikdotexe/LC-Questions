class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        used = [0]*len(nums)
        
        def backtrack():
            if len(temp)==len(nums) and temp not in res:
                res.append(temp.copy())
                return


            for i,num in enumerate(nums):
                if used[i]:
                    continue
                used[i]=1
                temp.append(num)
                backtrack()
                used[i]=0
                temp.pop()
                

        backtrack()
        return res