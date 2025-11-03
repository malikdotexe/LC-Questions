class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        max_time = neededTime[0]

        for i in range(1, len(colors)):
            #series of same color
            if colors[i] == colors[i - 1]:
                total += min(max_time, neededTime[i])
                max_time = max(max_time, neededTime[i])
            #new color 
            else:
                max_time = neededTime[i]
        
        return total
