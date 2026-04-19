from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in range(numCourses)]
        in_degree = [0] * numCourses
        is_prereq = [set() for _ in range(numCourses)]

        for pre, crs in prerequisites:
            adj[pre].add(crs)
            in_degree[crs] += 1
        
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while q:
            cur = q.popleft()
            for neighbor in adj[cur]:
                is_prereq[neighbor].add(cur)
                is_prereq[neighbor].update(is_prereq[cur])
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        return [u in is_prereq[v] for u, v in queries]
