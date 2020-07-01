from typing import List


class Solution:
  def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    ret = 0
    curr, start, end, total = 0, 0, 0, 0

    while curr < len(nums):
      try:
        curr_num = nums[curr]
        total += curr_num
        end = curr

        if total < s:
          continue
        else:
          # move start
          while end >= start:
            curr_len = end - start + 1
            if ret == 0:
              ret = curr_len
            elif curr_len < ret:
              ret = curr_len

            total -= nums[start]
            start += 1
            if total < s:
              break
      except Exception as e:
        raise e
      finally:
        curr += 1

    return ret

s = 7
nums = [2,3,1,2,4,3]
sol = Solution()
print(sol.minSubArrayLen(s, nums))
