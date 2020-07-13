from typing import List


class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    l = len(heights)
    stack = [-1]
    ans = 0

    for i in range(l):
      while heights[i] < 



heights = [2,1,5,6,2,3]
sol = Solution()
print(sol.largestRectangleArea(heights))
