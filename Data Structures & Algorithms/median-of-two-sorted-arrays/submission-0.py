class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2
        
        left = 0
        right = len(A)  # Can partition after the last element
        
        while left <= right:
            i = (left + right) // 2  # Number of elements from A on left side
            j = half - i              # Number of elements from B on left side
            
            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")
            
            if Aleft <= Bright and Bleft <= Aright:
                # Found correct partition
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1