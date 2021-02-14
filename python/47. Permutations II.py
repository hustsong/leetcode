from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # handle nums
        stat = {}
        for num in nums:
            stat[num] = stat.get(num, 0) + 1

        stat = sorted([(k, v) for k, v in stat.items()], key = lambda x: x[1])

        results = []
        def fill(stat, N, temp_result, results):
            if N >= len(stat):
                results.append(temp_result)
                return

            num, count = stat[N][0], stat[N][1]
            if N == len(stat) - 1:
                temp_result = [v if v is not None else num for v in temp_result]
                results.append(temp_result)

            temp_results = []
            fill_num(temp_results, temp_result[:], 0, num, count)

            for t in temp_results:
                fill(stat, N + 1, t, results)

        def fill_num(temp_results, temp_result, start, v, N):
            if len(temp_result) - start < N:
                return

            if N == 0:
                temp_results.append(temp_result)
                return

            if start >= len(temp_result):
                return

            for i in range(start, len(temp_result)):
                if temp_result[i] is not None:
                    continue
                
                new_temp_result = temp_result[:]
                new_temp_result[i] = v
                fill_num(temp_results, new_temp_result, i + 1, v, N - 1)

        fill(stat, 0, [None for _ in range(len(nums))], results)
        return results
        

nums = [1,2,3]
sol = Solution() 
print(sol.permuteUnique(nums))
