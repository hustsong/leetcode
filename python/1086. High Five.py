from typing import List
from collections import defaultdict


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        stat = defaultdict(list)
        for id, score in items: stat[id].append(score)
        return sorted([[id, (sum(sorted(scores, reverse=True)[:5])) // 5] for id, scores in stat.items()])

items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
sol = Solution()
print(sol.highFive(items))
