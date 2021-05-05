import heapq

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)


nums = [3,2,3,1,2,4,5,5,6]
k = 4
sol = Solution()
print(sol.findKthLargest(nums, k))
