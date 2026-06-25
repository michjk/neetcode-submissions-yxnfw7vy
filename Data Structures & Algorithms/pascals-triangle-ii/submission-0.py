class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        table = [[0] * (rowIndex + 1) for _ in range(rowIndex + 1)]
        table[0][0] = 1
        for r in range(1, rowIndex + 1):
            table[r][0] = 1
            table[r][r] = 1
            for c in range(1, r):
                table[r][c] = table[r - 1][c] + table[r - 1][c - 1]
        return table[rowIndex]
