from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        visited_1 = set()
        q1 = deque()
        
        for i in range(m):
            q1.append((i, 0))
        for j in range(1, n):
            q1.append((0, j))
        
        visited_2 = set()
        q2 = deque()
        for i in range(m):
            q2.append((i, n - 1))
        for i in range(n - 1):
            q2.append((m - 1, i))

        def solve(q):
            visited = set()
            while q:
                cur = q.popleft()
                visited.add(cur)
                cur_x, cur_y = cur
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_x, new_y = cur_x + dx, cur_y + dy
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                        continue
                    if (new_x, new_y) in visited:
                        continue
                    if heights[new_x][new_y] >= heights[cur_x][cur_y]:
                        q.append((new_x, new_y))
            return visited

        visited_1 = solve(q1)
        visited_2 = solve(q2)
        
        res = visited_1.intersection(visited_2)

        return [[i, j] for i, j in res]

