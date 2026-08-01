# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,path,res2):
        if not root:
            return
        path.append(str(root.val))
        if root.left:
            self.preorder(root.left,path,res2)
        if root.right:
            self.preorder(root.right,path,res2)
        if not root.left and not root.right:
            res2.append('->'.join(path))
   
        path.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res2 = []
        self.preorder(root,[],res2)
        return res2
        
    
    
        