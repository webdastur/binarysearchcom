# https://binarysearch.com/problems/Just-Average

from typing import List


class Solution:
    def solve(self, nums: List[int], k: int) -> bool:
        list_sum = sum(nums)
        for i in nums:
            if ((list_sum - i) / (len(nums) - 1)) == k:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve([1, 2, 3, 10], 2))
