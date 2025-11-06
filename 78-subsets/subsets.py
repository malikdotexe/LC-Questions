class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset= []
        def dfs(i):
            #base case
            if i>=len(nums):
                res.append(subset.copy())
                return
            #Decision 1 - To include the num
            subset.append(nums[i])
            dfs(i+1)
            #Decision 2 - To not include the num
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
            