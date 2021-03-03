from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0: return 0

        # get left max and right max for every height
        left_max, right_max = height[0], height[-1]
        left_max_arr, right_max_arr = list(), list()
        for i in range(len(height)):
            # left max
            if height[i] >= left_max:
                left_max = height[i]
            left_max_arr.append(left_max)

            # right max
            if height[-i - 1] >= right_max:
                right_max = height[-i - 1]
            right_max_arr.append(right_max)
        right_max_arr.reverse()

        return sum([min(left_max_arr[i], right_max_arr[i]) - h for i, h in enumerate(height)])


height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(height))
