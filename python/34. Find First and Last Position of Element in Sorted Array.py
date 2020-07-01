from typing import List


class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    l = len(nums)
    mid = int(l / 2) 
    return [self._find_first(0, mid), self._find_last(mid + 1, l)]

  def _find_first(self, start, end, target):
    if :
      return -1

  def _find_last(self, start, end, target):
    if :
      return -1

      


nums = [5,7,7,8,8,10]
target = 8
sol = Solution()
print(sol.searchRange(nums, target))
