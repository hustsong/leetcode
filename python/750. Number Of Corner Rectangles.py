from typing import List
from collections import Counter


class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m, n, ret = len(grid), len(grid[0]), 0
        couter = Counter()
        for i in range(m):
            for left, left_num in enumerate(grid[i]):
                if not left_num:
                    continue

                for right in range(left + 1, n):
                    if left_num + grid[i][right] == 2:
                        couter[left, right] += 1
                        ret += (couter[left, right] - 1)

        return ret


grid = [[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
sol = Solution()
print(sol.countCornerRectangles(grid))

