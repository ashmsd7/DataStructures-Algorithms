# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return (0,0)
            
            left_sum , left_count = dfs(root.left)
            right_sum , right_count = dfs(root.right)

            total_sum = root.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            if root.val == total_sum // total_count:
                res+=1

            return (total_sum , total_count)
        dfs(root)
        return res

        