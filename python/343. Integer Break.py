class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2

        product = 1
        while n:
            if n >= 5:
                product *= 3
                n -= 3
                continue
            
            if n == 4:
                product *= 4
            elif n == 3:
                product *= 3
            elif n == 2:
                product *= 2
            break

        return product


n = 10
sol = Solution()
print(sol.integerBreak(n))
