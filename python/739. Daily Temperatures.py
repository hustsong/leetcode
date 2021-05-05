from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # next array
        # next_array = [None] * 101
        # ans = [0] * len(T)
        # i = len(T) - 1
        # while i >= 0:
        #     try:
        #         curr_t = T[i]
        #         for j in range(curr_t + 1, 101):
        #             if next_array[j]:
        #                 dis = next_array[j] - i
        #                 if dis < ans[i] or ans[i] == 0:
        #                     ans[i] = dis
        #     finally:
        #         next_array[curr_t] = i
        #         i -= 1

        # stack
        stack = list()
        ans = [0] * len(T)
        i = len(T) - 1
        while i >= 0:
            curr_t = T[i]
            while stack:
                if T[stack[-1]] <= curr_t:
                    stack.pop()
                else:
                    break
            ans[i] = stack[-1] - i if stack else 0
            stack.append(i)
            i -= 1

        return ans


t = [73,74,75,71,69,72,76,73]
sol = Solution()
print(sol.dailyTemperatures(t))
