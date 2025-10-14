from collections import deque
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        #lenarr would contain length of all increasing subarrays
        lenarr = [1]
        l =1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                l+=1
            if nums[i]<=nums[i-1] or i==len(nums)-1:

                lenarr.append(l)

                #if we can make two increasing subarrays from the same subarray each of length k
                if lenarr[-1]//2>=k:
                    return True
                #elif there are two unique increasing subarrays adjacent
                elif len(lenarr)>1 and lenarr[-1]>=k and lenarr[-2]>=k:
                    return True
                l = 1
               
                
        return False