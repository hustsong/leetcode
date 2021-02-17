from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key= lambda x: x[0])
        prev = [-1, -1]
        for inter in intervals:
            if inter[0] < prev[1]:
                return False
            prev = inter
        return True


intervals = [[7,10],[2,4]]
sol = Solution()
print(sol.canAttendMeetings(intervals))
