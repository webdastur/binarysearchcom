from functools import cache


class Solution:
    def solve(self, n):
        return self.fib(n)

    @cache
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve(495))
