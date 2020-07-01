from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        base_ascii = ord('a')
        str_map = defaultdict(list)
        for s in strs:
            s_sign = [0] * 26
            for c in s:
                c_offset = ord(c) - base_ascii
                s_sign[c_offset] += 1
            str_map[tuple(s_sign)].append(s)

        return str_map.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(strs))
