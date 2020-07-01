from typing import List


class Solution:
  def maxProfit(self, k: int, prices: List[int]) -> int:
    if len(prices) <= 1 or k == 0:
      return 0

    # corner case
    if k >= len(prices) / 2:
      return sum(i - j 
        for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)

    note_k = [[0, prices[0]] for i in range(k)]

    for idx, price in enumerate(prices):
      for i in range(k):
        pos = -i - 1
        if pos == -k:
          pre_max_profit = 0
        else:
          pre_max_profit, _ = note_k[pos - 1]

        max_profit, buy = note_k[pos]
        if (price - buy) > max_profit:
          max_profit = price - buy
        if (price - pre_max_profit) < buy:
          buy = price - pre_max_profit

        note_k[pos] = [max_profit, buy]

    ret, _ = note_k[-1]
    return ret


prices = [3,2,6,5,0,3]
k = 1000000000000
sol = Solution()
print(sol.maxProfit(k, prices))
