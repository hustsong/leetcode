from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0

        ret = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(n):
            if (n - i) * m <= ret:
                continue

            row_stat = [0 for l in range(m)]
            for j in range(i, n):
                ones = 0
                col_ones = 0
                for k in range(m):
                    curr = matrix[k][j]
                    row_stat[k] += int(curr)
                    if row_stat[k] == (j - i + 1):
                        ones += 1
                        col_ones += 1
                        area = ones * (j - i + 1)
                        if area > ret:
                            ret = area
                    else:
                        ones = 0

                if col_ones == 0:
                    break

        return ret


m = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

sol = Solution()
print(sol.maximalRectangle((m)))
