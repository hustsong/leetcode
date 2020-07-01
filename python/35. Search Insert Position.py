from typing import List


class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    if nums[0] > target:
      return 0
    if nums[-1] < target:
      return len(nums)

    for idx, num in enumerate(nums):
      if num >= target:
        return idx


nums, target = [1,3,5,6], 5
sol = Solution()
print(sol.searchInsert(nums, target))
