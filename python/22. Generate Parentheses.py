from typing import List
from copy import deepcopy


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = ['(']
        self._do_generate(result, stack, n - 1, n)
        return result

    def _do_generate(self, result: List, old_stack: List, left: int, right: int):
        stack = deepcopy(old_stack)
        if left == right:
            if left > 0:
                stack.append('(')
                self._do_generate(result, stack, left - 1, right)
            elif right == 0:
                result.append(''.join(stack))
        else:
            if left > 0:
                stack.append('(')
                self._do_generate(result, stack, left - 1, right)
            if right > 0:
                stack = deepcopy(old_stack)
                stack.append(')')
                self._do_generate(result, stack, left, right - 1)


sol = Solution()
print(sol.generateParenthesis(3))
