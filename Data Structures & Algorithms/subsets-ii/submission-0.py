class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        def dfs(i, used):
            res.append(list(used))

            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                used.append(nums[j])
                dfs(j + 1, used)
                used.pop()
        
        dfs(0, [])
        return res