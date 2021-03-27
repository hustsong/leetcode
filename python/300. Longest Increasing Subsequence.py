from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ret = 1
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] >= nums[i]: continue
                dp[i] = dp[j] + 1 if dp[j] + 1 > dp[i] else dp[i]

            ret = dp[i] if dp[i] > ret else ret

        return ret


nums = [0,1,0,3,2,3]
sol = Solution()
print(sol.lengthOfLIS(nums))
