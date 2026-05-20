# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        prefix_id = in_id = 0

        def dfs(limit):
            nonlocal prefix_id, in_id
            if prefix_id >= len(preorder):
                return None
            if inorder[in_id] == limit:
                in_id += 1
                return None
            
            root = TreeNode(preorder[prefix_id])
            prefix_id += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)

            return root
        
        return dfs(float('inf'))
