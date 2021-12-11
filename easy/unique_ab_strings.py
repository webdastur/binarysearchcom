# https://binarysearch.com/problems/Unique-Ab-Strings

class Solution:
    def solve(self, s: str) -> int:
        return 2 ** sum([1 for x in s if x == 'a'])


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve('aaa'))
