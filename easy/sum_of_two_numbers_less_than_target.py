import math
from typing import List


class Solution:
    def solve(self, nums: List[int], target: int):
        nums.sort()
        left, right = 0, len(nums) - 1
        result = -math.inf
        while left < right:
            if nums[left] + nums[right] < target:
                result = max(result, nums[left] + nums[right])
                left += 1
            else:
                right -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve([5, 1, 2, 3], 4))
