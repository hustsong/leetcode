from typing import List
from heapq import heapify, heappop, heappush
from math import sqrt
from collections import defaultdict


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = list()
        heapify(heap)

        cord_map = defaultdict(list)
        for p in points:
            distance = -sqrt(abs(p[0]) ** 2 + abs(p[1]) ** 2)
            cord_map[distance].append(p)
            if len(heap) < k:
                heappush(heap, distance)
                continue

            if distance < heap[0]:
                continue

            heappop(heap)
            heappush(heap, distance)
        
        res = list()
        while heap:
            ps = cord_map[heappop(heap)]
            if len(ps) + len(res) <= k:
                res.extend(ps)
            else:
                res.extend(ps[:k - len(res)])
                break

        return res


points = [[1,0],[0,1]]
k = 2
sol = Solution()
print(sol.kClosest(points, k))
