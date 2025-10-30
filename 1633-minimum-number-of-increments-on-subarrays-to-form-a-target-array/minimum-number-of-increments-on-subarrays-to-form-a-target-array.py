#Simpler Approach
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        ans = target[0]
        for i in range(1,n):
            if target[i]>target[i-1]:
                ans+=target[i]-target[i-1]
        return ans
        


                
