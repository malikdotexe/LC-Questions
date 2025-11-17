class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        r=0
        while r<len(nums)-1:
            gap = 0
            if nums[r]==1:
                r+=1
                while r<len(nums) and nums[r]==0:
                    gap+=1
                    r+=1
                r-=1
                #edge case if nums end with 0
                if r==len(nums)-1 and nums[r]==0:
                    continue
                    
                if gap<k:
                    return False
            r+=1
        return True


            