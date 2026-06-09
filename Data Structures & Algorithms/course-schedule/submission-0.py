from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for v, u in prerequisites:
            adj_list[u].append(v)
            degree[v] += 1
        
        q = deque([u for u in range(numCourses) if degree[u] == 0])

        while q:
            u = q.popleft()
            for v in adj_list[u]:
                if degree[v] > 0:
                    degree[v] -= 1
                if degree[v] == 0:
                    q.append(v)

        return all(item == 0 for item in degree)


        
        
        
