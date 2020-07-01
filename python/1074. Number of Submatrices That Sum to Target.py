from typing import List
from collections import defaultdict


class Solution:
  def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
    rows, cols = len(matrix), len(matrix[0])

    # traversal every submaxtrix
    # for all submatrices having the same left index and right index
    # record current sum in a dict from top to bottom
    count = 0
    for col in range(cols):
      row_sums = [0] * rows
      for y in range(col, cols):
        submaxtrix_sums = defaultdict(int)
        submaxtrix_sums[0] = 1
        row_sum = 0
        for x in range(rows):
          row_sums[x] += matrix[x][y]
          row_sum += row_sums[x]
          count += submaxtrix_sums[row_sum - target]
          submaxtrix_sums[row_sum] += 1

    return count


matrix = [[1,-1],[-1,1]]
target = 0
sol = Solution()
print(sol.numSubmatrixSumTarget(matrix, target))
