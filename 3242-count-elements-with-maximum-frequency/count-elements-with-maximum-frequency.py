class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxfreq = max(count.values())
        res = 0
        for v in count.values():
            if v == maxfreq:
                res += v
        return res