from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = Counter(S)
        most_common = counter.most_common()
        _, count = most_common[0]
        if count > (len(S) // 2 + len(S) % 2):
            return ''

        res = [None for _ in range(len(S))]
        idx = [i for i in range(0, len(S), 2)] + [i for i in range(1, len(S), 2)]

        ii = 0
        for n, count in most_common:
            while count:
                res[idx[ii]] = n
                count -= 1
                ii += 1

        return ''.join(res)
        

S = "vvvlo"
sol = Solution()
print(sol.reorganizeString(S))
