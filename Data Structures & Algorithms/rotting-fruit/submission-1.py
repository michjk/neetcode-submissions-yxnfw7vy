from collections import deque

DIRECTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 2:
                    q.append((x, y))
                if grid[x][y] == 1:
                    fresh += 1
        res = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in DIRECTIONS:
                    new_x, new_y = x + dx, y + dy

                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                        continue

                    if grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        q.append((new_x, new_y))
                        fresh -= 1
            res += 1

        return res if fresh == 0 else -1
