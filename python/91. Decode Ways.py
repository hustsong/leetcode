from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache
        def walk(s, start):
            if start >= len(s):
                return 1
            
            # 1 digit
            res = 0
            C = int(s[start:start + 1])
            if C != 0:
                res += walk(s, start + 1)

            # 2 digits
            if start < len(s) - 1:
                C = int(s[start:start + 2])
                if 9 < C <= 26:
                    res += walk(s, start + 2)
            return res
        return walk(s, 0)


s = "111111111111111111111111111111111111111111111"
sol = Solution()
print(sol.numDecodings(s))

