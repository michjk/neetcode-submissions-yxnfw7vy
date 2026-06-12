class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}

        for idx, c in enumerate(s):
            last_idx[c] = idx
        
        size = 0
        max_idx = 0
        res = []
        for idx, c in enumerate(s):
            size += 1
            max_idx = max(max_idx, last_idx[c])
            if last_idx[c] == idx and idx == max_idx:
                res.append(size)
                size = 0
        
        return res
            