from typing import List


class Solution:
  def pancakeSort(self, A: List[int]) -> List[int]:
    target = A
    source = [i + 1 for i in range(len(A))]
    l = len(A)

    order = []
    pos = -1
    while True:
      if -pos > l:
        break

      if source[pos] == target[pos]:  # no move
        pass
      elif source[0] == target[pos]:  # move one step
        # move source
        head = source[:l + pos + 1]
        head.reverse()
        source = head + source[l + pos + 1:]
        order.append(l + pos + 1)
      else: # move two steps
        # find target
        i = 0
        while source[i] != target[pos]:
          i += 1

        # 1st move
        head = source[:i + 1]
        head.reverse()
        source = head + source[i + 1:]
        order.append(i + 1)

        # 2nd move
        head = source[:l + pos + 1]
        head.reverse()
        source = head + source[l + pos + 1:]
        order.append(l + pos + 1)

      pos -= 1

    order.reverse()
    return order

A = [3,2,4,1]
# A = [2, 4, 1, 3]
sol = Solution()
print(sol.pancakeSort(A))
