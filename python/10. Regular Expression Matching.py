class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 or len(p) == 0:
            return False

        # parse pattern
        patterns = []
        curr_p = ''
        for c in p:
            if c != '*':    # start new pattern
                if curr_p != '':
                    patterns.append(curr_p)
                curr_p = c
            else:
                curr_p += '*'
        patterns.append(curr_p)
        patterns = [(p[0], p[1], ) if len(p) > 1 else (p, 1,) for p in patterns]

        dp = [[0 for i in range(len(s))] for j in range(len(patterns))]

        for char_pos in range(len(s)):
            for pattern_pos in range(len(patterns)):
                char = s[char_pos]
                (c, n) = patterns[pattern_pos]
                if c in (char, '.', ):
                    dp[pattern_pos][char_pos] = 1

        print(dp)

        # start point
        start = None
        for pattern_pos in range(len(patterns)):
            if dp[pattern_pos][0] == 1:
                start = pattern_pos
        if start is None:
            return False

        # traversal dp
        x, y = 0, pattern_pos
        while True:
            if


s = 'aa'
p = 'aa'
sol = Solution()
print(sol.isMatch(s, p))
