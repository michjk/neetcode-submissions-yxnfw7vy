class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefix = [[cell for cell in row] for row in matrix]
        m = len(prefix)
        n = len(prefix[0])
        for i in range(1, m):
            prefix[i][0] += prefix[i - 1][0]

        for i in range(1, n):
            prefix[0][i] += prefix[0][i - 1]

        for row in range(1, m):
            for col in range(1, n):
                prefix[row][col] += prefix[row - 1][col] + prefix[row][col - 1] - prefix[row - 1][col - 1]
        self.prefix = prefix  
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.prefix[row2][col2]
        if row1 > 0:
            res -= self.prefix[row1 - 1][col2]
        if col1 > 0:
            res -= self.prefix[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            res += self.prefix[row1 - 1][col1 - 1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)