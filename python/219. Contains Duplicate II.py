from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_pos = {}
        for i, n in enumerate(nums):
            if n not in last_pos:
                last_pos[n] = i
                continue
            
            if i - last_pos[n] <= k:
                return True

            last_pos[n] = i

        return False


nums = [1,2,3,1,2,3]
k = 2
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))
