import heapq
from typing import List


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # priority = -x + y (highest)
        # heapq priority = -(-x + y) = x - y (lowest)
        q = []
        res = -float('inf')
        for x, y in points:
            while q and x - q[0][1] > k:
                heapq.heappop(q)
            if q:
                res = max(res, x + y - q[0][0])
            heapq.heappush(q, (x - y, x))

        return res


points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1
sol = Solution()
print(sol.findMaxValueOfEquation(points, k))
