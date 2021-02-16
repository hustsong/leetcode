from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, count = {}, {}
        res, degree = 0, 0
        for i, n in enumerate(nums):
            first.setdefault(n, i)
            if count.get(n, 0) + 1 > degree:
                degree = count.get(n, 0) + 1
                res = i - first[n] + 1
            elif count.get(n, 0) + 1 == degree:
                res = min(res, i - first[n] + 1)
            count[n] = count.get(n, 0) + 1
        return res


nums = [2,1,1,2,1,3,3,3,1,3,1,3,2]
sol = Solution()
print(sol.findShortestSubArray(nums))