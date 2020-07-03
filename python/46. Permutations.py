from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 1:
            return [nums]
        if n == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]

        orders = self._order_template(nums[1:])
        orders = [[nums[0]] + order for order in orders]

        ret = []
        for order in orders:
            for i in range(n):
                curr = order[i:] + order[:i]
                ret.append(curr)

        return ret

    def _order_template(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1:
            return [[nums[0]]]

        ret = []
        for i in range(n):
            base = [nums[i]]
            orders = self._order_template([num for num in nums if num != nums[i]])
            for order in orders:
                ret.append(base + order)

        return ret


nums = [1, 2, 3]
sol = Solution()
print(sol.permute(nums))
