from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if m != n:
            return False
        
        cnt1 = Counter(s)
        cnt2 = Counter(t)

        if len(cnt1) != len(cnt2):
            return False
        
        for key in cnt1:
            if key not in cnt2 or cnt1[key] != cnt2[key]:
                return False
        return True
