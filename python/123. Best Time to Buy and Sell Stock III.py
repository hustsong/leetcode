from typing import List


class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    if len(prices) <= 1:
      return 0

    forward = []
    backward = []

    min_price = prices[0]
    max_profit = 0
    for price in prices:
      curr_profit = price - min_price
      if curr_profit >= max_profit:
        max_profit = curr_profit
      if price <= min_price:
        min_price = price
      forward.append(max_profit)

    max_price = prices[-1]
    max_profit = 0
    ret_max_profit = 0
    for idx, price in enumerate(prices[::-1]):
      curr_profit = max_price - price
      if curr_profit >= max_profit:
        max_profit = curr_profit
      if price >= max_price:
        max_price = price
      backward.append(max_profit)

      if idx == 0:
        continue

      curr_ret_max_profit = max_profit + forward[-idx - 1]
      if curr_ret_max_profit >= ret_max_profit:
        ret_max_profit = curr_ret_max_profit

    return ret_max_profit

  def maxProfit2(self, prices: List[int]) -> int:
    if len(prices) <= 1:
      return 0

    buy1, buy2, profit1, profit2 = prices[0], prices[0], 0, 0

    for price in prices:
      profit2 = max(profit2, price - buy2)
      buy2 = min(buy2, price - profit1) # cost = price - profit1
      profit1 = max(profit1, price - buy1)
      buy1 = min(price, buy1)

    return profit2



prices = [3,3,5,0,0,3,1,4]
sol = Solution()
print(sol.maxProfit(prices))
print(sol.maxProfit2(prices))

