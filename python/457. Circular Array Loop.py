from typing import List


class Solution:
  def circularArrayLoop(self, nums: List[int]) -> bool:
    label, curr_loop = [0] * len(nums), [0] * len(nums)
    not_idx, side, l = 0, 0, len(nums)
    

    while True:
      if not_idx >= l:
        break

      curr = not_idx
      side = 1 if nums[not_idx] > 0 else -1
      curr_loop = [0] * len(nums)
      twos = 0
      while True:
        curr_side = 1 if nums[curr] > 0 else -1
        # break
        if side != curr_side:
          break

        # loop
        if twos == 1 and curr_loop[curr] == 2:
          break
        if twos == 2:
          return True

        # walk
        label[curr] = 1
        curr_loop[curr] += 1
        if curr_loop[curr] == 2:
          twos += 1
        curr += nums[curr]
        if curr >= l:
          curr = int(curr % l)
        if curr <= -l:
          curr = int(curr % l)

      # not_idx
      while label[not_idx] == 1:
        not_idx += 1
        if not_idx == l:
          break

    return False


nums = [-2,-3,-9]
sol = Solution()
print(sol.circularArrayLoop(nums))
