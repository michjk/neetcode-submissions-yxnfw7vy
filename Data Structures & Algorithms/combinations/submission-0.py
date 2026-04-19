class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(pos, comb):
            if len(comb) == k:
                res.append(list(comb))
            
            for i in range(pos, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        
        backtrack(1, [])
        return res