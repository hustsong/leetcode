class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        stat = dict()
        for c in s:
            stat[c] = stat.get(c, 0) + 1

        pivots = 0
        for c, count in stat.items():
            if count % 2 == 1:
                pivots += 1
                if pivots >= 2:
                    return False

        return True


sol = Solution()
s = 'aaaabbbb'
print(sol.canPermutePalindrome(s))
