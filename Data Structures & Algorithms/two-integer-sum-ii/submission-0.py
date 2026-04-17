class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            tmp = numbers[l] + numbers[r]
            print(l, r, tmp)
            if tmp == target:
                return [l + 1, r + 1]
            if tmp < target:
                l += 1
            else:
                r -= 1
        
        return [l, r]