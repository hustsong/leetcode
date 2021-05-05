from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)

        ans = 0
        for box_number, box_unit in boxTypes:
            for _ in range(box_number):
                if truckSize:
                    ans += box_unit
                    truckSize -= 1
                else:
                    return ans

        return ans

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
sol = Solution()
print(sol.maximumUnits(boxTypes, truckSize))
