from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for v, u in prerequisites:
            adj_list[u].append(v)
            in_degree[v] += 1
        
        q = deque()
        for u in range(numCourses):
            if in_degree[u] == 0:
                q.append(u)

        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in adj_list[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        
        return res if all(u == 0 for u in in_degree) else []


