class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)

        #prefix  
        pre = nums[:]
        for i in range(1,n):
            pre[i]+=pre[i-1]
        
        #postfix
        post =nums[:]
        for i in range(n-2,-1,-1):
            post[i]+=post[i+1]
        ans = 0

        for i in range(n):
            if nums[i]==0:
                if pre[i]==post[i]:
                    ans+=2
                elif pre[i]==post[i]+1 or post[i]==pre[i]+1:
                    ans+=1
        return ans
