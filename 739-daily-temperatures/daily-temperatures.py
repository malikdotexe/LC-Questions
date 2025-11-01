class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i,n in enumerate(temperatures):
            while stack and stack[-1][0]<n:
                res[stack[-1][1]] = i- stack[-1][1]
                stack.pop()
            stack.append([n,i])
        return res