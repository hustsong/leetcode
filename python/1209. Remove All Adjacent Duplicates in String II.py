class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i, c in enumerate(s):
            if not stack or c != stack[-1][0]:
                stack.append((c, 1))
            else:
                stack.append((c, stack[-1][1] + 1))

            # pops
            if stack[-1][1] == k:
                stack = stack[:-k]


        return ''.join([c for c, _ in stack])


s = "pbbcggttciiippooaais"
k = 2
sol = Solution()
print(sol.removeDuplicates(s, k))
