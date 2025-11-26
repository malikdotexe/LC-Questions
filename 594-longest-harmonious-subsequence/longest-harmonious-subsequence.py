class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxlen = 0
        for key,value in count.items():
            if key-1 in count:
                maxlen = max(maxlen,count[key]+count[key-1])
        print(count)
        return maxlen
