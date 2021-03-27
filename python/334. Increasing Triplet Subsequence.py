from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_pair_max = None
        curr_min = nums[0]
        for num in nums:
            if min_pair_max is not None and num > min_pair_max:
                return True

            if num > curr_min:
                if not min_pair_max or num < min_pair_max:
                    min_pair_max = num
            if num < curr_min:
                curr_min = num

        return False


nums = [2,1,5,0,4,6]
sol = Solution()
print(sol.increasingTriplet(nums))
