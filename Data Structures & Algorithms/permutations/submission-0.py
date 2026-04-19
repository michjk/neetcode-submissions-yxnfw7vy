class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(pos, used, perm):
            if pos == n:
                res.append(list(perm))
                return
            
            for i in range(n):
                if i in used:
                    continue
                used.add(i)
                perm.append(nums[i])
                backtrack(pos + 1, used, perm)
                used.remove(i)
                perm.pop()
        
        backtrack(0, set(), [])
        return res
