from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        while q:
            x, y, d = q.popleft()
            if grid[x][y] not in [-1, 0] and d > grid[x][y]:
                continue
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                    continue
                if grid[new_x][new_y] in [-1, 0] or grid[new_x][new_y] <= d + 1:
                    continue
                grid[new_x][new_y] = d + 1
                q.append((new_x, new_y, d + 1))
                
