from typing import List


class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    return self._do_combination(k, n, 1)

  def _do_combination(self, k: int, n: int, start: int) -> List[List[int]]:
    ret = []

    if (10 - start) < k:
      return [[]]

    if n <= 0 or k <= 0:
      return [[]]

    if k == 1 and n > 9:
      return [[]]

    for i in range(start, 10):
      if i > n:
        break

      if k == 1 and i == n:
        return [[i]]

      curr_sum = [i]
      sums = self._do_combination(k - 1, n - i, i + 1)
      for iter_sum in sums:
        if len(iter_sum) != (k - 1):
          continue

        ret.append(curr_sum + iter_sum)

    return ret

k = 3
n = 18
sol = Solution()
print(sol.combinationSum3(k, n))
