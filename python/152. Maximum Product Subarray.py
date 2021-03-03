from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0: return 0

        curr_max, curr_min = nums[0], nums[0]
        result = curr_max
        for i in range(1, l):
            curr = nums[i]
            temp_max = max(curr, curr_max * curr, curr_min * curr)
            curr_min = min(curr, curr_max * curr, curr_min * curr)

            curr_max = temp_max
            result = max(result, curr_max)
        
        return result

    # def maxProduct(self, nums: List[int]) -> int:
    #     l = len(nums)
    #     if l == 0: return 0

    #     max = -float('inf')
    #     for i in range(l):  # left
    #         accumulate = 1
    #         for j in range(i, l):  # right
    #             accumulate *= nums[j]
    #             max = accumulate if accumulate > max else max

    #     return max

nums = [2,3,-2,4]
sol = Solution()
print(sol.maxProduct(nums))
