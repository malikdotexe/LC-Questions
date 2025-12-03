class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def Valid(left,right,curr):
            if not curr:
                return True
            if not (curr.val>left and curr.val<right):
                return False
            
            return Valid(left, curr.val, curr.left) and Valid(curr.val, right, curr.right)

        return Valid(float("-inf"),float("inf"),root)