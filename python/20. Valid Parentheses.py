class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if len(stack) > 0 and stack[-1] + c in ("()", "{}", "[]", ):
                stack.pop()
                continue
            stack.append(c)

        return True if len(stack) == 0 else False


s = "{[]}"
sol = Solution()
print(sol.isValid(s))
