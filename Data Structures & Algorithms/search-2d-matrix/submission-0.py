import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ls = [cell for row in matrix for cell in row]
        idx = bisect.bisect_left(ls, target)
        return (idx < len(ls) and ls[idx] == target)