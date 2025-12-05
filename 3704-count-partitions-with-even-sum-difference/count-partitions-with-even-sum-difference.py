class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        postfix = nums.copy()
        n = len(nums)
        for i in range(n-2,-1,-1):
            postfix[i]+=postfix[i+1]
        count = 0
        presum = 0
        for i in range(n-1):
            presum +=nums[i]
            partsum = presum - postfix[i+1]
            if partsum%2==0:
                count+=1
        return count