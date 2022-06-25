# https://binarysearch.com/problems/3-6-9

class Solution:
    def solve(self, n):
        result = []

        for i in range(1, n + 1):
            if i % 3 == 0 or any(map(lambda x: x in f"{i}", ["3", "6", "9"])):
                result.append("clap")
            else:
                result.append(f"{i}")
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve(16))