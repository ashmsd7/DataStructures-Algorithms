# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        if not root:
            return []
        res = []

        while queue:
            size = len(queue)
            sum_val = 0
            for _ in range(size):
                node = queue.popleft()
                sum_val += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sum_val/size)
        return res
        
                    


        