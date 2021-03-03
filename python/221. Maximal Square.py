from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        area = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                curr = int(matrix[i][j])
                if curr == 0:
                    continue
                
                dp[i][j] = min([dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]]) + 1
                area = dp[i][j] ** 2 if dp[i][j] ** 2 > area else area

        return area


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
sol = Solution()
print(sol.maximalSquare(matrix))
