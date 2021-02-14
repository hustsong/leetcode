from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        stat = [0] * 60
        for t in time:
            stat[t % 60] += 1

        res = stat[0] * (stat[0] - 1) // 2 + stat[30] * (stat[30] - 1) // 2 
        for i in range(1, 30):
            res += stat[i] * stat[60 - i]

        return res

sol = Solution()
time = [30,20,150,100,40]
print(sol.numPairsDivisibleBy60(time))
