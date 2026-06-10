class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(n // 2):
                matrix[j][i], matrix[n - j - 1][i] = matrix[n - j - 1][i], matrix[j][i]
        
        print(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        print(matrix)
