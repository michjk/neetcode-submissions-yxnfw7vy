# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        node_2_sum = defaultdict(int)

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            node_2_sum[node] = left + right + node.val

            return max(left, right) + node.val
        
        dfs(root)
        return max(node_2_sum.values())