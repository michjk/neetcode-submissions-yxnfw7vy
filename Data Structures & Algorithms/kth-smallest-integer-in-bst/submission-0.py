# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def solve(node: Optional[TreeNode]):
            if not node:
                return None
            nonlocal k
            left = solve(node.left)
            k -= 1
            if k == 0:
                return node.val
            right = solve(node.right)

            if left is not None:
                return left
            if right is not None:
                return right
            return None
        res = solve(root)
        return res
