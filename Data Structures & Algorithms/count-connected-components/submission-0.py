class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {u:[] for u in range(n)}
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(u):
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    dfs(v)
        
        res = 0
        for u in range(n):
            if u not in visited:
                visited.add(u)
                dfs(u)
                res += 1

        return res