# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def is_identical(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        if tree1.val != tree2.val:
            return False
        
        Left = self.is_identical(tree1.left,tree2.left)
        Right = self.is_identical(tree1.right,tree2.right)

        return Left and Right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stacker = [root]
        while stacker:
            node = stacker.pop()
            if self.is_identical(node,subRoot):
                return True
            if node.left:
                stacker.append(node.left)
            if node.right:
                stacker.append(node.right)
        return False
    
        