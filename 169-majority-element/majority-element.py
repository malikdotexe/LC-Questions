class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=0
        majority = nums[0]
        for num in nums:
            if num==majority:
                a+=1
            else:
                a-=1
            if a<1:
                majority =num
                a+=1
            
        return majority

