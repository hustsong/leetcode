from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pass

    def _order_template(self, n: int) -> List[List[int]]:
        if n == 1:
            return [0]


nums = [1, 2, 3]
sol = Solution()
print(sol.permute(nums))
