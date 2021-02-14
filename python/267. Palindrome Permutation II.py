from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        if not s:
            return []

        char_stat = dict()
        for c in s:
            char_stat[c] = char_stat.get(c, 0) + 1

        pivots = []
        texts = []
        for c, count in char_stat.items():
            if count % 2 == 0:
                texts.append((c, count))
            else:
                pivots.append((c, count))
        
        if len(pivots) >= 2:
            return []

        pivot, pivot_count = pivots[0] if len(pivots) == 1 else ('', 0)
        texts = [(c, int(count / 2)) for c, count in texts]
        if pivot_count > 2:
            texts.append((pivot, int((pivot_count - 1) / 2)))

        texts.sort(key = lambda x: x[1])

        results = []
        def fill(results, result, N):
            if N >= len(texts):
                results.append(result)
                return
            
            # the last c
            c, count = texts[N]
            if N == len(texts) - 1:
                result = [c if rc is None else rc for rc in result]
                results.append(result)
                return
            
            # continue fillling
            temp_results = []
            fill_num(temp_results, result[:], 0, c, count)
            for t in temp_results:
                fill(results, t, N + 1)

        def fill_num(temp_results, temp_result, start, v, N):
            if len(temp_result) - start < N or start > len(temp_result):
                return

            if N == 0:
                return temp_results.append(temp_result)

            for i in range(start, len(temp_result)):
                if temp_result[i] is not None:
                    continue

                new_temp_result = temp_result[:]
                new_temp_result[i] = v
                fill_num(temp_results, new_temp_result, i + 1, v, N - 1)
        
        fill(results, [None for i in range(sum([t[1] for t in texts]))], 0)

        return [''.join(r + [pivot] + r[::-1])  for r in results]

s = 'abbab'
sol = Solution()
print(sol.generatePalindromes(s))
