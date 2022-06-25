# https://binarysearch.com/problems/Guess-the-Root

class Solution:
    def solve(self, n):
        return int(n ** (1 / 2))


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve(26))
    print(solution.solve(9))