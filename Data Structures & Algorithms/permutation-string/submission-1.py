from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False
        
        mp1 = Counter(s1)
        mp2 = defaultdict(int)
        l = 0
        for r in range(m):
            mp2[s2[r]] += 1
            if r >= n:
                mp2[s2[l]] -= 1
                l += 1
            found = True
            for k, v in mp1.items():
                if mp2[k] != v:
                    found = False
                    break
            if found:
                return True
            
        return False
