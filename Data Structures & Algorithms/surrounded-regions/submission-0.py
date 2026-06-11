class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        border = set()
        
        def dfs(r: int, c: int):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if (r, c) in border:
                return
            if board[r][c] != "O":
                return
            
            border.add((r, c))

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dx, c + dy)
        
        for r in range(m):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][n - 1] == "O":
                dfs(r, n - 1)
        
        for c in range(n):
            if board[0][c] == "O":
                dfs(0, c)
            if board[m - 1][c] == "O":
                dfs(m - 1, c)

        for r in range(m):
            for c in range(n):
                if (r, c) not in border:
                    board[r][c] = "X"
        


