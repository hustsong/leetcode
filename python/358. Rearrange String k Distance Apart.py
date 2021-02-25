from collections import Counter


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0 or len(s) == 0: return s

        counter = Counter(s).most_common()
        
        k -= 1
        res = []
        pushed, task_count = 0, len(s)
        while True:
            i, curr = 0, [None] * (k + 1)
            for idx, (task, count) in enumerate(counter):
                if count == 0:
                    break
                if i > k:
                    break
                curr[i] = task
                i += 1
                pushed += 1
                count -= 1
                counter[idx] = task, count

            res += curr
            if pushed == task_count:
                break
            
            # sort
            counter.sort(key = lambda x : x[1], reverse = True)

            while counter[-1][1] == 0:
                counter.pop()

        while res[-1] is None:
            res.pop()

        return ''.join(res) if len(res) == len(s) else ''


s = "aaadbbcc"
k = 3
sol = Solution()
print(sol.rearrangeString(s, k))
