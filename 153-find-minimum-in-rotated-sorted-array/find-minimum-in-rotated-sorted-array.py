class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0 
        r=len(nums)-1
        mini = nums[0]
        while l<=r:
            mid = l+(r-l)//2
            #If we are in Part(II) - the unrotated part
            mini = min(mini,nums[mid])
            if nums[mid]<nums[len(nums)-1]:
                r= mid-1
            #If we are in Part(I) - the rotated part
            elif nums[mid]>nums[len(nums)-1]:
                l= mid+1    
            elif nums[mid]==nums[len(nums)-1]:
                return nums[mid]
        return mini
            
            
            
                