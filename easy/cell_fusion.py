# https://binarysearch.com/problems/Cell-Fusion

import heapq
from typing import List


class Solution:
    def solve(self, cells: List[int]):
        cells = [-x for x in cells]
        heapq.heapify(cells)
        while len(cells) > 1:
            first, second = -heapq.heappop(cells), -heapq.heappop(cells)
            if first != second:
                heapq.heappush(cells, -((first + second) // 3))
        return -cells[0] if cells else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve([10, 30, 30, 20]))
    print(solution.solve([10, 30, 30, 20, 40, 50]))
