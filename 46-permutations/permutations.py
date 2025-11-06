# Example - BOAT
# when we chose B as our first letter , after which we called the backtrack function we ran the loop on the complete word BOAT but with our duplication skipping line we were able to skip b so we only had option to chose from {OAT} 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def backtrack():
            #basecase
            if len(temp)==len(nums):
                res.append(temp.copy())
                return
            
            #trying each number
            for num in nums:
                #skipping already present number in temp
                if num in temp:
                    continue
                temp.append(num)
                backtrack()
                temp.pop()    
        backtrack()
        return res