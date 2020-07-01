from typing import List


class Solution:
  def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    alen = len(A)
    for i in range(alen):
      s, e = 0, alen - 1
      while s <= e:
        


        s += 1
        e -= 1

A = [[1,1,0],[1,0,1],[0,0,0]]
sol = Solution()
print(sol.flipAndInvertImage(A))
