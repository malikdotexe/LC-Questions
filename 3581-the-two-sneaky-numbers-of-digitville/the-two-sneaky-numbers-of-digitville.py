class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashset = set()
        res = []
        count = 0
        for num in nums:
            if num in hashset:
                res.append(num)
                count+=1
            if count==2:
                return res
            hashset.add(num)
        