class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        arr = matrix
        n = len(arr)
        m = len(arr[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = [m, n - 1]

        r, c, d = 0, -1, 0
        while steps[d % 2]:
            for i in range(steps[d % 2]):
                r += dirs[d][0]
                c += dirs[d][1]
                res.append(arr[r][c])
            steps[d % 2] -= 1
            d += 1
            d %= 4

        return res