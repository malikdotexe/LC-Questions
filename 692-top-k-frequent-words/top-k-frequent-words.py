class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqmap = Counter(words)
        freqmap = dict(sorted(freqmap.items()))
        bucketlist = [[] for i in range(len(words)+1)]

        for key,value in freqmap.items():
            bucketlist[value].append(key)
        res = []

        for i in range(len(bucketlist)-1,0,-1):
            for word in bucketlist[i]:
                res.append(word)
                if len(res)==k:
                    return res