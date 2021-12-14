# https://binarysearch.com/problems/Strictly-Alternating-List
from typing import List


class Solution:
    def solve(self, nums: List[int]) -> bool:
        is_increasing = nums[0] < nums[1]

        if not is_increasing:
            return False

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                if not is_increasing:
                    is_increasing = True
            if nums[i - 1] > nums[i]:
                if is_increasing:
                    is_increasing = False

            if nums[i - 1] == nums[i]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve([1, 2, 5, 7, 4, 1, 6, 8, 3, 2]))
    print(solution.solve([1, 1, 2, 3, 2, 1]))
    print(solution.solve([5, 3, 1, 5, 7]))
