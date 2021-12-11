# https://binarysearch.com/problems/Toeplitz-Matrix

from typing import List


class Solution:
    def solve(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i - 1][j - 1] != matrix[i][j]:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve([
        [0, 1, 2],
        [3, 0, 1],
        [4, 3, 0],
        [5, 4, 3]
    ]))
