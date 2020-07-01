from typing import List


class Solution:
  def sortArrayByParity(self, A: List[int]) -> List[int]:
    left, right = 0, len(A) - 1
    while left < right:
      if int(A[left] % 2) == 0:
        left += 1
        continue

      if int(A[right] % 2) == 1:
        right -= 1
        continue

      # swap
      temp = A[left]
      A[left] = A[right]
      A[right] = temp
      left += 1
      right -= 1

    return A


nums = [3,1,2,4]
sol = Solution()
print(sol.sortArrayByParity(nums))
