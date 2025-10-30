#Similar to largest rectangle in histogr
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        #ns = next smaller
        ns = [-1]*n
        stack = []
        for i in range(n-1,-1,-1):
            while stack and target[i]<=stack[-1]:
                stack.pop()
            if not stack:
                ns[i] = 0
            else:
                ns[i] = stack[-1]
            stack.append(target[i])
        #ps = previous smaller
        ps = [-1]*n
        stack = []
        for i in range(n):
            while stack and target[i]<stack[-1]:
                stack.pop()
            if not stack:
                ps[i]=0
            else:
                ps[i]= stack[-1]
            stack.append(target[i])
        ans = 0
        #traversing target
        for i in range(n):
            if i>0 and target[i] == target[i-1]:
                continue
            else:
                ans += target[i] - max(ns[i],ps[i])
        return ans
                    


                
