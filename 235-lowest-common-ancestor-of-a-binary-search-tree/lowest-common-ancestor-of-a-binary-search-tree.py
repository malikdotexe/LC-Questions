# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            #If both values are larger then go towards right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            #elif both values are smaller then go towards left subtree 
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            #if one value is larger and other smaller, its the dividing node which inturn is LCA
            else:
                return cur