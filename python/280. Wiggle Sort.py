from typing import List


class Solution:
  def wiggleSort(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def swap(nums, i, j):
      t = nums[i]
      nums[i] = nums[j]
      nums[j] = t

    for i, num in enumerate(nums):
      if i % 2 == 1 and nums[i - 1] > nums[i]:
        swap(nums, i, i - 1)
      elif i % 2 == 0 and i > 0 and nums[i - 1] < nums[i]:
        swap(nums, i, i - 1)

nums = [3,5,2,1,6,4]
sol = Solution()
sol.wiggleSort(nums)
print(nums)
