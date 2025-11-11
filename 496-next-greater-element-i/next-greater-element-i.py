
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ng = {}
        stack = []
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            if stack:
                ng[nums2[i]]=stack[-1]
            if not stack:
                ng[nums2[i]]=-1
            stack.append(nums2[i])
        res = []
        print(ng)
        for num in nums1:
            res.append(ng[num])
        return res




