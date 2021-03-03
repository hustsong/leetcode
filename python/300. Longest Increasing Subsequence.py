from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        res = -float('inf')
        for i, num in enumerate(nums):
            min_val, max_val = num, num
            left, right = i, i
            curr_len = 1
            while True:
                if left > 0:
                    left -= 1
                    if nums[left] < min_val:
                        curr_len += 1
                        min_val = nums[left]
                if right < l - 1:
                    right += 1
                    if nums[right] > max_val:
                        curr_len += 1
                        max_val = nums[right]

                if right - left >= l - 1:
                    break
            res = curr_len if curr_len > res else res
        
        return res


nums = [0,1,0,3,2,3]
sol = Solution()
print(sol.lengthOfLIS(nums))
