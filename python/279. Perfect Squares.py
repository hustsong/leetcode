class Solution:
    def numSquares(self, n: int) -> int:
        num_min_squares = {}
        num_min_squares[0] = 0
        num_min_squares[1] = 1

        for i in range(n + 1):
            sqrt = i ** 0.5
            if sqrt % 1 == 0.0:
                num_min_squares[i] = 1
                continue

            curr_min = i
            sqrt = int(sqrt)
            while sqrt:
                squares = 1 + num_min_squares[i - sqrt * sqrt]
                if squares < curr_min:
                    curr_min = squares
                sqrt -= 1
            num_min_squares[i] = curr_min

        return num_min_squares[n]

n = 9997
sol = Solution()
print(sol.numSquares(n))
