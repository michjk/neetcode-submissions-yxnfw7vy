class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        used = set()
        def backtrack(cnt: int):
            if cnt == len(nums):
                res.append(list(cur))
                return
            
            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                cur.append(nums[i])
                backtrack(cnt + 1)
                used.remove(nums[i])
                cur.pop()
        
        backtrack(0)
        return res
                
