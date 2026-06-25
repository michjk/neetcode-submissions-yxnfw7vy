class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {val: key for key, val in enumerate(nums2)}
        res = []

        for num in nums1:
            start = mp[num]
            found = False
            for i in range(start + 1, len(nums2)):
                if nums2[i] > nums2[start]:
                    res.append(nums2[i])
                    found = True
                    break
            if not found:
                res.append(-1)
        return res
