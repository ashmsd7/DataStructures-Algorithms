# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(root,targetSum):
            if not root:
                return 

            path.append(root.val)

            if root.left is None and root.right is None and targetSum == root.val :
                res.append(path.copy())
            
            backtrack(root.left,targetSum - root.val)
            backtrack(root.right,targetSum - root.val)

            path.pop()

        backtrack(root,targetSum)

        return res


    

        