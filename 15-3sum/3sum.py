class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res= []
        for a in range(n):
            b= a+1
            c = n-1
            if a>0 and nums[a]==nums[a-1]:
                continue
            while b<c:
                sum = nums[a]+nums[b]+nums[c]
                if sum>0:
                    c-=1
                elif sum<0:
                    b+=1
                else:
                    res.append([nums[a],nums[b],nums[c]])
                    b+=1
                    c-=1
                    while b<c and nums[b]==nums[b-1]:
                        b+=1
        return res