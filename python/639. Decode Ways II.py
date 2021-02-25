from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache
        def walk(s, start):
            if start >= len(s):
                return 1
            
            # 1 digit
            res = 0
            c = s[start:start + 1]
            if c == '*':
                res += 9 * walk(s, start + 1)
            else:
                C = float(c)
                if C != 0:
                    res += walk(s, start + 1)

            # 2 digits
            if start < len(s) - 1:
                cs = s[start:start + 2]
                if '*' not in cs:
                    C = float(cs)
                    if 9 < C <= 26:
                        res += walk(s, start + 2)
                else:
                    times = 1
                    if cs == '**':
                        times = 15
                    elif cs[0] == '*':
                        times = 1 if float(cs[1]) > 6 else 2
                    elif cs[1] == '*':
                        if float(cs[0]) == 1:
                            times = 9
                        elif float(cs[0]) == 2:
                            times = 6
                        else:
                            times = 0
                    res += times * walk(s, start + 2)
            return res
        return walk(s, 0)


s = "******"
sol = Solution()
print(sol.numDecodings(s))

