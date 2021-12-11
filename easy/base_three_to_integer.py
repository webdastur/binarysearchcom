class Solution:
    def solve(self, s: str) -> int:
        result = 0

        s = s[::-1]

        for i in range(len(s)):
            result += int(s[i]) * (3 ** i)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve('21'))
