class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(i):
            #base case
            if i==len(nums):
                res.append(subset.copy())
                return
            
            #Choices

            #Choice 1 - To include the num
            subset.append(nums[i])
            dfs(i+1)
            subset.pop() #backtrack
            #Choice 2 -To not include the num
            #the next num should be a unique value
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)

        #initiate
        dfs(0)
        return res
            
