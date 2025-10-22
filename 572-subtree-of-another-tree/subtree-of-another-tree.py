class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #A null tree can always be a subtree of other
        if not subRoot:
            return True
        #if main tree is empty 
        if not root:
            return False
        #if both trees are identical starting from this node
        if self.isSame(root,subRoot):
            return True
        #otherwise, check recursively if subRoot exists in the left or right subtree of root
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    #Helper function from previous question
    def isSame(self,first,second):
        if not first and not second:
            return True
        if not first or not second:
            return False
        if first.val != second.val:
            return False
        return (self.isSame(first.left,second.left) and self.isSame(first.right,second.right))