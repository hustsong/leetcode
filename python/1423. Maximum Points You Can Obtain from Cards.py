from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_score = curr_score = sum(cardPoints[:k])
        for i in range(k):
            curr_score = curr_score + cardPoints[-i - 1] - cardPoints[k - 1 - i]
            max_score = curr_score if curr_score > max_score else max_score

        return max_score

cardPoints = [96,90,41,82,39,74,64,50,30]
k = 8
sol = Solution()
print(sol.maxScore(cardPoints, k))
