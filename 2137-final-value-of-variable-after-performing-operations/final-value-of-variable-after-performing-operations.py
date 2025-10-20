class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        #LC daily 20 Oct 2025
        ans = 0
        for ops in operations:
            if ops =="++X" or ops=="X++":
                ans+=1
            elif ops == "--X" or ops=="X--":
                ans-=1
        return ans