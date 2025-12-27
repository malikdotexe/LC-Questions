class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0 
        for i in range(len(happiness)):
            h = happiness[i]
            if i==0:
                res+=h
                dec = 1
                k-=1
            else:
                h= h-dec
                if h<0:
                    h=0
                res+=h
                dec+=1
                k-=1
            if k==0:
                break
        return res
    