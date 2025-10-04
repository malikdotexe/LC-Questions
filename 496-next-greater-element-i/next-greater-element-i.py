
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums1)
        idxmap = {x:i for i,x in enumerate(nums1)}
        
        stack = []
        for n in nums2:
            while stack and n>stack[-1]:
                val = stack.pop()
                res[idxmap[val]] = n
            if n in nums1:
                stack.append(n)
        return res

            
