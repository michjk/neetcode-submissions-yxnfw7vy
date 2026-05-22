"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = {}

        def dfs(node: Optional['Node']):
            if not node:
                return None
            if node in mp:
                return mp[node]
            new_node = Node(node.val)
            mp[node] = new_node

            for neighbor in node.neighbors:
                next_node = dfs(neighbor)
                if next_node:
                    new_node.neighbors.append(next_node)
            
            return new_node
        
        return dfs(node)
            