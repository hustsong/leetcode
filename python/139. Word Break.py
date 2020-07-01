from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = {w for w in wordDict}
        sl = len(s)
        record = {0: 1}

        for i in range(sl):
            if i not in record:
                continue

            for j in range(i + 1, sl + 1):
                if j in record:
                    continue

                curr_w = s[i:j]
                if curr_w in words:
                    record[j] = 1

        return True if sl in record else False


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
sol = Solution()
print(sol.wordBreak(s, wordDict))
