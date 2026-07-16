class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        lines = []
        length = 0
        i = 0

        while i < len(words):
            if length + len(lines) + len(words[i]) <= maxWidth:
                length += len(words[i])
                lines.append(words[i])
                i += 1
            else:
                extra_spaces = maxWidth - length
                space_cnt = max(1, len(lines) - 1)
                remainder = extra_spaces % space_cnt
                space = extra_spaces // space_cnt
                for j in range(max(1, len(lines) - 1)):
                    lines[j] += " " * space
                    if remainder:
                        lines[j] += " "
                        remainder -= 1
                res.append("".join(lines))
                lines = []
                length = 0
        
        last_line = " ".join(lines)
        trailing_space = maxWidth - len(last_line)
        res.append(last_line + " " * trailing_space)
        return res