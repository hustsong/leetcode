from typing import List


class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    # n th value in m th row = C(n -1, m - 1)
    ret = []
    row_m = rowIndex + 1
    pivot = round(row_m)
    for i in range(row_m):
      if i > pivot:
        ret.append(ret[row_m - i - 1])
        continue

      row_n = i + 1
      product, factorial = 1, 1
      for j in range(row_n - 1):
        product *= (row_m - j - 1)
        factorial *= (j + 1)

      if row_n == 1:
        ret.append(1)
      else:
        ret.append(int(product / factorial))

    return ret


# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6=C(6, 1) 15=C(6, 2) 20=C(6, 3) 15 6 1
# 1 7 21 35=C(7, 3) 35 21 7 1

sol = Solution()
print(sol.getRow(6))
