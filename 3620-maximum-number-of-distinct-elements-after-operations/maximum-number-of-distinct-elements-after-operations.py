class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:

        nums.sort()
        #initializing maxnum as lower bound of the first number
        maxnum = nums[0]-k
        distinctcount = 0
        for num in nums:
            upperbound = num+k
            lowerbound = num-k
            #if the maxnum is within range
            if maxnum<lowerbound:
                maxnum = lowerbound
       
            if maxnum<=upperbound:
                maxnum+=1
                distinctcount+=1
        return distinctcount
        