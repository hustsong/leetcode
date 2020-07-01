from typing import List


class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    curr, ret, l = 0, 0, len(cost)
    while True:
      if -curr >= (l - 1):
        break

      if cost[curr - 1] >= cost[curr - 2]:
        curr -= 2
      else:
        curr -= 1

      ret += cost[curr]

    return ret


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
sol = Solution()
print(sol.minCostClimbingStairs(cost))
