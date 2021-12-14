# https://binarysearch.com/problems/Check-Palindrome

class Solution:
    def solve(self, s: str) -> bool:
        return s == s[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve('racecar'))
