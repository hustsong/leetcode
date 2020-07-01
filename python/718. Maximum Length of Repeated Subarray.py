from typing import List


class Solution:
  def findLength(self, A: List[int], B: List[int]) -> int:
    i, j = len(A), len(B)

    dp = [[0 for k in range(j + 1)] for k in range(i + 1)]
    length = 0
    for m in range(i):
      for n in range(j):
        x, y = m + 1, n + 1
        pre_len =  dp[m][n]
        if A[m] == B[n]:
          curr_len = pre_len + 1
          dp[x][y] = curr_len
          if curr_len > length:
            length = curr_len

    return length


A = [1,2,3,2,1]
B = [3,2,1,4,7]
sol = Solution()
print(sol.findLength(A, B))
