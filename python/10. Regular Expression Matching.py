class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 or len(p) == 0:
            return False

        # split patterns
        ps = []
        prev_c = ''
        for c in p:
            if c == '*':
                ps.append(prev_c + c)
                prev_c = ''
            else:
                if prev_c: ps.append(prev_c)
                prev_c = c
        if prev_c: ps.append(prev_c)

s = 'aa'
p = 'a*'
sol = Solution()
print(sol.isMatch(s, p))
