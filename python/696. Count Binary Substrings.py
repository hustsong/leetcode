class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        last_c = None
        last_c_count, pos, ret = 0, 0, 0

        while pos < len(s):
            c = s[pos]
            if last_c is None or c == last_c:
                last_c = c
                last_c_count += 1
                pos += 1
                continue

            # forward
            f_pos = pos
            while True:
                if s[f_pos] == c:
                    ret += 1
                f_pos += 1
                if f_pos == len(s) or s[f_pos] != c or f_pos - pos + 1 > last_c_count:
                    last_c = s[f_pos - 1]
                    last_c_count = f_pos - pos
                    pos = f_pos
                    break

        return ret


s = '10101'
sol = Solution()
print(sol.countBinarySubstrings(s))
