class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = 0
        pos_diag = 0
        neg_diag = 0
        board = [["."] * n for i in range(n)]
        res = []
        
        def backtrack(r: int):
            nonlocal col, pos_diag, neg_diag
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if (col & (1 << c)) or (pos_diag & (1 << (r + c))) or (neg_diag & (1 << (r - c + n))):
                    continue
                col ^= (1 << c)
                pos_diag ^= (1 << (r + c))
                neg_diag ^= (1 << (r - c + n))
                board[r][c] = "Q"

                backtrack(r + 1)

                col ^= (1 << c)
                pos_diag ^= (1 << (r + c))
                neg_diag ^= (1 << (r - c + n))
                board[r][c] = "."
        
        backtrack(0)

        return res