class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = [False] * n
        pos_diag = [False] * (n * 2)
        neg_diag = [False] * (n * 2)
        board = [['.'] * n for _ in range(n)]
        res = []
        
        def backtrack(r: int):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if col[c] or pos_diag[r + c] or neg_diag[r - c + n]:
                    continue
                col[c] = True
                pos_diag[r + c] = True
                neg_diag[r - c + n] = True
                board[r][c] = "Q"

                backtrack(r + 1)

                col[c] = False
                pos_diag[r + c] = False
                neg_diag[r - c + n] = False
                board[r][c] = "."
        
        backtrack(0)

        return res