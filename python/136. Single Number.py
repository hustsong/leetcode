from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = nums[0]
        for i in range(1, len(nums)):
            ret ^= nums[i]

        return ret

nums = [4,1,2,1,2]
sol = Solution()
print(sol.singleNumber(nums))
