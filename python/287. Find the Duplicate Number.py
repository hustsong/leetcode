from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # rec = dict()
        # for num in nums:
        #     if num in rec:
        #         return num
        #     rec[num] = 1

        for i in range(len(nums)):
            n = nums[i]
            if i == n - 1:
                continue
            
            j, m = n - 1, n
            while True:
                if nums[j] is None:
                    nums[j] = m
                    break
                if nums[j] == m:
                    return m

                temp = nums[m - 1]
                nums[m - 1] = m
                nums[i] = None
                j = temp -1
                m = temp


nums = [1,1,2]
sol = Solution()
print(sol.findDuplicate(nums))
