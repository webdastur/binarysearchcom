# https://binarysearch.com/problems/Range-Query-on-a-List

from typing import List


class RangeSum:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = nums.copy()
        self.prefix_sum.insert(0, 0)
        for i in range(1, len(self.prefix_sum)):
            self.prefix_sum[i] += self.prefix_sum[i - 1]

    def total(self, i, j):
        return self.prefix_sum[j] - self.prefix_sum[i]


if __name__ == '__main__':
    range_sum = RangeSum([1, 2, 5, 0, 3, 7])
    print(range_sum.total(0, 3))
    print(range_sum.total(1, 5))
