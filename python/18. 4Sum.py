from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def NSum(l, r, N, target, result, results):
            nlen = r - l + 1
            if N > nlen or N < 2 or target > nums[r] * N or target < nums[l] * N:
                return

            if N == 2:  # two sum on a sorted list
                while l < r:
                    curr_sum = nums[l] + nums[r]
                    if curr_sum > target:
                        r -= 1
                    elif curr_sum < target:
                        l += 1
                    else:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
            else:
                for i in range(l, r + 1):
                    if i == l or (i > l and nums[i -1] != nums[i]):
                        NSum(i + 1, r, N - 1, target - nums[i], 
                            result + [nums[i]], results)
        
        nums.sort()
        results = []
        NSum(0, len(nums) - 1, 4, target, [], results)
        return results


nums = [1,0,-1,0,-2,2]
target = 0
sol = Solution()
print(sol.fourSum(nums, target))
