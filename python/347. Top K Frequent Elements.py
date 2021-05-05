from typing import List
from heapq import heappush, heappop
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = dict()
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        
        rec = defaultdict(list)
        heap = []
        for num, count in num_counts.items():
            heappush(heap, count)
            rec[count].append(num)
            if len(heap) > k:
                heappop(heap)
            
        ret = list()
        heap = sorted(list(set(heap)))

        heap.sort(reverse=True)
        for count in heap:
            ret.extend(rec[count])
            if len(ret) >= k:
                return ret[:k]

        return ret


nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
k = 10
sol = Solution()
print(sol.topKFrequent(nums, k))
