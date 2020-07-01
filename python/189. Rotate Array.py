from typing import List


class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    offset = k % l
    
    # start from nums[l - 1]
    start = l - 1
    curr, last_num = (start + k) % l, nums[start]
    count = 1
    while True:
      temp = nums[curr]
      nums[curr] = last_num
      last_num = temp

      if curr == start:
        if count == l:
          break
        curr -= 1
        start = curr
        last_num = nums[curr]

      count += 1
      curr = (curr + k) % l


nums = [1,2,3,4,5,6]
k = 2
sol = Solution()
sol.rotate(nums, k)
print(nums)


[1,2,3,4,5,6,7]
[1,2,7,4,5,6,None]
[1,2,7,4,5,3,None]
[1,6,7,4,5,3,None]
[1,6,7,4,2,3,None]
[5,6,7,4,2,3,None]
[5,6,7,1,2,3,None]
[5,6,7,1,2,3,4]
