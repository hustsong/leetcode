from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                left = i + 1
            if nums[i] > nums[i + 1]:
                break

        for i in range(len(nums))[::-1]:
            if nums[i] > nums[i - 1] and :
                right = i - 1
            if nums[i] < nums[i - 1]:
                break

        if right == 0 or nums[0] == nums[-1]:
            return 0

        return right - left + 1


nums = [1,2,3,4]
sol = Solution()
print(sol.findUnsortedSubarray(nums))

