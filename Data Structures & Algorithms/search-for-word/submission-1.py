class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(x, y, pos):
            if (x < 0 or
                x >= m or 
                y < 0 or 
                y >= n or 
                pos >= len(word)
                or board[x][y] != word[pos]):
                return False
            if pos == len(word) - 1:
                return True
            board[x][y] = "#"
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if dfs(x + dx, y + dy, pos + 1):
                    return True
            board[x][y] = word[pos]
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
