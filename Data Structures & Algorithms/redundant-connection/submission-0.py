class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = [i for i in range(n + 1)]
        self.rank = [1 for _ in range(n + 1)]
    
    def find(self, u):
        if self.p[u] == u:
            return u
        self.p[u] = self.find(self.p[u])
        return self.p[u]

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return True
        if self.rank[u] > self.rank[v]:
            self.p[v] = u
            self.rank[u] += 1
        else:
            self.p[u] = v
            self.rank[v] += 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        
        res = []
        for u, v in edges:
            if uf.union(u, v):
                res.append([u, v])
        
        return res[-1]