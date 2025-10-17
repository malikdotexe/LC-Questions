# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root]) 
        depth = 0
        while queue:
            depth+=1
            for _ in range(len(queue)):
                current = queue.popleft()
                print(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return depth