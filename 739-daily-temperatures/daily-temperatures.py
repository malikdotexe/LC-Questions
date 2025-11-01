class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res  = []
        #monotonic decreasing
        stack = []
        n = len(temperatures)
        for i in range(n-1,-1,-1):
            while stack and stack[-1][0]<=temperatures[i]:
                stack.pop()
            #No temp found greater than our current temp
            if not stack:
                    res.append(0)
            else:
                res.append((stack[-1][1]-i))
            stack.append([temperatures[i],i])

        res.reverse()		
        return res
