class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset= {}
        for i,num in enumerate(nums):
            if (target-num) in numset:
                return [numset[target-num],i]
            numset[num] = i
            