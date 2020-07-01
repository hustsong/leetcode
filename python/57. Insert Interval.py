from typing import List


class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if len(intervals) == 0:
      return [newInterval]

    if newInterval[0] > intervals[-1][-1]:
      intervals.append(newInterval)
      return intervals

    new_intervals = []
    start, end = newInterval
    closed = True
    inserted = False
    not_closed_start, not_closed_start = None, None
    for interval in intervals:
      iter_start, iter_end = interval
      if end < iter_start and closed and not inserted:
        new_intervals.append(newInterval)
        inserted = True

      if iter_end < start or iter_start > end:
        if not  closed:
          new_intervals.append([not_closed_start, not_closed_end])
          not_closed_start, not_closed_start = None, None
          inserted = True

        new_intervals.append(interval)
        closed = True
        continue

      # overlap
      if closed:  # new interval
        not_closed_start = min(start, iter_start)
        not_closed_end = max(end, iter_end)
        closed = False
      else: # inside a interval
        not_closed_end = max(not_closed_end, iter_end)
        continue

    if not closed:
      new_intervals.append([not_closed_start, not_closed_end])

    return new_intervals


intervals = [[2,4],[5,7],[8,10],[11,13]]
newInterval = [3,6]
sol = Solution()
print(sol.insert(intervals, newInterval))
