class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mindiff=float("inf")
        for i in range(len(nums)):
            #skip duplicates for a
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                curr = nums[i]+nums[l]+nums[r]
                diff = target-curr
                if abs(diff)<abs(mindiff):
                    mindiff = diff
                    ans = curr

                if curr<target:
                    l+=1
                elif curr>target:
                    r-=1
                else:
                    return curr
        return ans