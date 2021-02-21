from typing import List


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        stat = [[None for _ in range(8)] for _ in range(4)]
        for num in nums:
            l, p, v = num // 100, num % 100 // 10, num % 10
            stat[l - 1][p - 1] = v

        sum = 0
        for num in nums:
            l, p, v = num // 100, num % 100 // 10, num % 10
            # get parent, left, right
            if l == 1:
                path_sum = 0
            else:
                path_sum = stat[l - 1 - 1][(p - 1) // 2]
            
            if l == 4 or (stat[l][2 * (p - 1)] is None and stat[l][2 * (p - 1) + 1] is None):
                sum += (path_sum + v)

            stat[l - 1][p - 1] = path_sum + v

        return sum


nums = [113, 221]
sol = Solution()
print(sol.pathSum(nums))
