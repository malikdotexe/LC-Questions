class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
       k = k%len(nums)
       pivot = len(nums)-k       
       nums[k:],nums[:k] = nums[:pivot],nums[pivot:]


        