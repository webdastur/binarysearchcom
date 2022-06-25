# https://binarysearch.com/problems/Check-if-Number-Is-Perfect-Square

class Solution:
    def solve(self, n):
        return int(n ** (1 / 2)) ** 2 == n


if __name__ == '__main__':
    solution = Solution()

    print(solution.solve(25))
    print(solution.solve(26))
