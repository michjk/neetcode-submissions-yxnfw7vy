class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        m = len(matrix)
        n = len(matrix[0])
        
        def dfs(x, y):
            if (x, y) in dp:
                return dp[(x, y)]
            
            res = 0
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if matrix[x][y] < matrix[nx][ny]:
                    res = max(res, dfs(nx, ny))
            dp[(x, y)] = res + 1
            return dp[(x, y)]
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res
            