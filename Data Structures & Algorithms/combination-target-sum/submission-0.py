class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def solve(pos: int, rem: int):
            if pos == len(nums) or rem < 0:
                return
            if rem == 0:
                res.append(list(cur))
            for i in range(pos, len(nums)):
                cur.append(nums[i])
                solve(i, rem - nums[i])
                cur.pop()
        solve(0, target)
        return res

