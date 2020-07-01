from typing import List


class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    hlen = len(heights)
    dp = [[-1 for _ in range(hlen)] for _ in range(hlen)]  # min from i to j

    max_area = 0
    for i in range(hlen):
      for j in range(hlen):
        if j < i:
          continue

        if j == i:
          min_h = heights[i]
        else:
          min_h = min(dp[i][j - 1], heights[j])

        dp[i][j] = min_h
        curr_area = (j - i + 1) * dp[i][j]
        if curr_area > max_area:
          max_area = curr_area

    return max_area

  def largestRectangleArea2(self, heights: List[int]) -> int:
    heights.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(heights)):
      while heights[i] < heights[stack[-1]]:
        h = heights[stack.pop()]
        w = i - stack[-1] - 1
        ans = max(ans, h * w)

        print(i, h, w)

      stack.append(i)
    heights.pop()
    return ans

heights = [2,1,5,6,2,3]
sol = Solution()
print(sol.largestRectangleArea(heights))
print(sol.largestRectangleArea2(heights))

