from typing import List
from functools import lru_cache


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mem = set()

        def area(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])
                and (i, j) not in mem and grid[i][j]):
                return 0
            mem.add((i, j))
            return 1 + area(i - 1, j) + area(i + 1, j) + \
                    area(i, j + 1) + area(i, j - 1)

        return max([area(i, j) 
                    for i in range(len(grid)) 
                    for j in range(len(grid[0]))])


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
sol = Solution()
print(sol.maxAreaOfIsland(grid))
