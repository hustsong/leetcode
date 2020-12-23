from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        positive    = [num for num in nums if num < 0]
        zero        = [num for num in nums if num == 0]
        negative    = [num for num in nums if num > 0]

        


nums = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(nums))