class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for item in strs:
            n = len(item)
            res.append(f"{n}#{item}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        n = 0
        i = 0
        print(s)
        while i < len(s):
            print(i, s[i])
            if s[i] == "#":
                res.append(s[i + 1: i + 1 + n])
                i = i + n
                n = 0
            else:
                n = n * 10 + int(s[i])
            i += 1
        return res


