from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # after end of arr
        if (arr[-1] - len(arr)) < k:
            return arr[-1] + (k - (arr[-1] - len(arr)))

        for i in range(len(arr)):
            curr = arr[i]
            if (curr - (i + 1)) < k:
                continue
            
            return curr - (curr - (i + 1) - k) - 1



arr = [1,2,3,4]
k = 2
sol = Solution()
print(sol.findKthPositive(arr, k))
