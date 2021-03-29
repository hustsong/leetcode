class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        num_stack, op_stack = [], []
        
        last_i = 0
        ops = {'+', '-', '*', '/'}
        md_ops = {'*', '/'}
        for i, c in enumerate(s):
            if c in ops or i == len(s) - 1:
                if c in ops:
                    num_stack.append(s[last_i:i])
                    last_i = i + 1
                else:
                    num_stack.append(s[last_i:])

                # compute '*' and '/'
                if op_stack and op_stack[-1] in md_ops:
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    op = op_stack.pop()
                    if op == '*':
                        num_stack.append(int(num1) * int(num2))
                    elif op == '/':
                        num_stack.append(int(num1) // int(num2))

                if c in ops:
                    op_stack.append(c)

        res = int(num_stack[0])
        for i, op in enumerate(op_stack):
            res += int(num_stack[i + 1]) * (1 if op == '+' else -1)

        return res


s = "3 / 2"
sol = Solution()
print(sol.calculate(s))
