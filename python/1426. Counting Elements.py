from typing import List
from collections import Counter


class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = Counter(arr)
        res = 0
        for n in counter:
            if (n - 1) in counter:
                res += counter[n - 1]
        return res





