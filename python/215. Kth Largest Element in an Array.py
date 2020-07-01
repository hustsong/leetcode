from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = 0
        low, high = 0, len(nums) - 1

        while True:
            # traversal
            while low < high:
                if nums[high] > nums[pivot]:
                    high -= 1
                    continue
                if nums[low] < nums[pivot]:
                    low += 1
                    continue
                if nums[high] < nums[pivot]:
                    temp = nums[pivot]
                    nums[pivot] = nums[high]
                    pivot = high


            if pivot == k:
                return nums[pivot]

nums = [3,2,1,5,6,4]
k = 2
sol = Solution()
print(sol.findKthLargest(nums, k))
