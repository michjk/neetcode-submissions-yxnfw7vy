DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])

        visited = set()

        def dfs(x, y):
            if (x, y) in visited:
                return 0
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0
            if grid[x][y] == 0:
                return 0
            visited.add((x, y))
            s = 1
            for dx, dy in DIRS:
                s += dfs(x + dx, y + dy)
            return s
        
        for x in range(m):
            for y in range(n):
                if (x, y) not in visited:
                    res = max(res, dfs(x, y))
        
        return res
                    
        