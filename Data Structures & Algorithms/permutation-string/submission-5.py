from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:len(s1)])  # fix 1: len(s1), not len(cnt1)
        
        matched = sum(1 for c in map(chr, range(ord('a'), ord('z') + 1))
                      if cnt1[c] == cnt2[c])

        left = 0
        for right in range(len(s1), len(s2)):
            if matched == 26:
                return True

            # Expand right
            cnt2[s2[right]] += 1
            if cnt1[s2[right]] == cnt2[s2[right]]:
                matched += 1
            elif cnt1[s2[right]] + 1 == cnt2[s2[right]]:
                matched -= 1

            # Shrink left
            cnt2[s2[left]] -= 1
            if cnt1[s2[left]] == cnt2[s2[left]]:
                matched += 1
            elif cnt1[s2[left]] - 1 == cnt2[s2[left]]:  # fix 2
                matched -= 1
            left += 1

        return matched == 26