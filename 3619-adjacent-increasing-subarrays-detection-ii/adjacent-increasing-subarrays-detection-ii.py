class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:

        ans = 0
        firstlen = 1
        l = 0
        r =1
        while r<len(nums):
            if nums[r]>nums[r-1]:
                r+=1
                firstlen=r-l
                #Our answer could also be a single increasing subarray divided into two parts
                ans = max(ans,firstlen//2)
                
            elif nums[r]<=nums[r-1]:
                l = r
                r += 1
                secondlen = 1
                while r<len(nums) and nums[r]>nums[r-1]:
                    r+=1
                    secondlen = r-l
                    #if the firstlen is greater our answer would be length of second sub array
                    if firstlen>=secondlen:
                        ans = max(ans,secondlen)
                    #if the firstlen becomes less than secondlen then its better to check for making two subarray from the same second array
                    else:
                        ans = max(ans,secondlen//2)
                #now our second subarray becomes our first  
                firstlen =secondlen    
        #There is no point in returning 0 as a single element could always be considered a subarray
        return max(ans,1)
                  