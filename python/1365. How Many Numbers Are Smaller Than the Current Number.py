from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        count_map = dict()
        count = 0
        for i, n in enumerate(sorted_nums):
            if n not in count_map:
                count_map[n] = count
            count += 1

        return [count_map[n] for n in nums]


nums = [7,7,7,7]
sol = Solution()
print(sol.smallerNumbersThanCurrent(nums))
