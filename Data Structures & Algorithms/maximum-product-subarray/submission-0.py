class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_n = float("-inf")
        cur = 1

        for i in range(len(nums)):
            cur *= nums[i]
            max_n = max(max_n, cur)
            if cur == 0:
                cur = 1
        
        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            cur *= nums[i]
            max_n = max(max_n, cur)
            if cur == 0:
                cur = 1
        
        return max_n

