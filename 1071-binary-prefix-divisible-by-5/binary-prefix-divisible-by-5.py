class Solution:
       def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans, b = [], 0
        for a in A:
            b = b << 1 | a
            ans.append(b % 5 == 0)
        return ans