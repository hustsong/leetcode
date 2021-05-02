from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        hmax, vmax = 1, 1
        pre_h, pre_v = 0, 0
        for h in horizontalCuts + [h]:
            curr_h = h - pre_h
            hmax = curr_h if curr_h > hmax else hmax
            pre_h = h

        for v in verticalCuts + [w]:
            curr_v = v - pre_v
            vmax = curr_v if curr_v > vmax else vmax
            pre_v = v
        
        return hmax * vmax % ((10 ** 9) + 7)


h = 5
w = 4
horizontalCuts = [3,1]
verticalCuts = [1]
sol = Solution()
print(sol.maxArea(h, w, horizontalCuts, verticalCuts))
