from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ret = list()
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                n = nums[left]
                left += 1
            else:
                n = nums[right]
                right -= 1
            ret.append(n ** 2)
        return ret[::-1]


