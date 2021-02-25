from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0 or len(tasks) == 0:
            return len(tasks)

        counter = Counter(tasks).most_common()
        
        res = []
        pushed, task_count = 0, len(tasks)
        while True:
            i, curr = 0, [None] * (n + 1)
            for idx, (task, count) in enumerate(counter):
                if count == 0:
                    continue
                if i > n:
                    break
                curr[i] = task
                i += 1
                pushed += 1
                count -= 1
                counter[idx] = task, count

            res += curr
            if pushed == task_count:
                break
            counter.sort(key = lambda x : x[1], reverse = True)

        while res[-1] is None:
            res.pop()

        return len(res)


tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
n = 1
sol = Solution()
print(sol.leastInterval(tasks, n))
