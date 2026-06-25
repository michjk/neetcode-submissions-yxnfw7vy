class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        left = n - 2
        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1
        if left >= 0:
            right = n - 1
            while nums[right] <= nums[left]:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        nums[left + 1:] = nums[left + 1:][::-1]

