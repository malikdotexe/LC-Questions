class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        bucketarr = [[] for i in range(len(nums)+1)]
        for num,freq in hashmap.items():
            bucketarr[freq].append(num)
        res = []

        for i in range(len(bucketarr)-1,-1,-1):
            for num in bucketarr[i]:
                res.append(num)
                if len(res)==k:
                    return res