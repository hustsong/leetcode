class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        if l <= 1: return l

        dp = [[0 for _ in range(l)] for _ in range(l)]
        
        res = 0
        for i in range(l - 1, -1, -1):  # left char
            for j in range(l - 1, -1, -1):  # right char
                if i > j:
                    continue
                
                # str start
                if i == j:
                    dp[i][j] = 1
                    res += 1
                    continue
                if i + 1 == j and s[i] == s[j]:
                    dp[i][j] = 1
                    res += 1
                    continue

                prev = dp[i + 1][j - 1]
                if prev == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    res += 1

        return res


s = "abc"
sol = Solution()
print(sol.countSubstrings(s))
