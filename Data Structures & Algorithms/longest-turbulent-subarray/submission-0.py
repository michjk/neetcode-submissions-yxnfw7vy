class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = [1]
        
        def turbulance(mode: bool):
            n = len(arr)
            i = 0
            start = 0
            cond = (1, 0) if mode else (0, 1)
            while i < n - 1:
                if (
                    (i % 2 == cond[0] and arr[i] < arr[i + 1]) or
                    (i % 2 == cond[1] and arr[i] > arr[i + 1])
                ):
                    res[0] = max(res[0], i + 1 - start + 1)
                else:
                    start = i + 1
                i += 1
    
        
        turbulance(True)
        turbulance(False)

        return res[0]
