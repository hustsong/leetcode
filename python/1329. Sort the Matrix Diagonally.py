from typing import List


class Solution:
  def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
    h = len(mat)
    w = len(mat[0])
    starts = []

    # from bottom-left to top-right
    for y in range(h - 1):
      starts.append((h - 1 - y, 0))
    for x in range(w):
      starts.append((0, x))

    for x, y in starts:
      start_x, start_y = x, y
      nums = []

      while (x < h) and (y < w):
        nums.append(mat[x][y])
        x += 1
        y += 1
      nums = sorted(nums)
      idx = 0
      while (start_x < h) and (start_y < w):
        mat[start_x][start_y] = nums[idx]
        idx += 1
        start_x += 1
        start_y += 1

    return mat

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
sol = Solution()
print(sol.diagonalSort(mat))
