from typing import List
from collections import defaultdict

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        for n, c in count.items():
            if k == 0:
                res += (1 if c > 1 else 0)
                continue

            target = n + k
            if target in count:
                res += 1

        return res

nums = [-1,-2,-3]
k = 1
sol = Solution()
print(sol.findPairs(nums, k))
