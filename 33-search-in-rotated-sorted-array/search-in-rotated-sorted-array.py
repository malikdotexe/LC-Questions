class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1
        while l<=r:
            mid = l+(r-l)//2

            if target == nums[mid]:
                return mid
            #sorted array
            elif nums[mid]<=nums[-1]:
                if target<nums[mid]:
                    r = mid -1
                else:
                    if target<=nums[-1]:
                        l = mid+1
                    else:
                        r = mid-1
            #rotated array
            else:
                if target>nums[mid]:
                    l=mid+1
                else:
                    if target<nums[0]:
                        l = mid+1
                    else:
                        r = mid-1
                        
                
        return -1