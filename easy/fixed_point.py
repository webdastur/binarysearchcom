# https://binarysearch.com/problems/Fixed-Point
import sys


class Solution:
    def solve(self, nums):
        low = 0
        high = len(nums) - 1
        result = sys.maxsize

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == mid:
                result = min(result, mid)
                high = mid - 1
            if nums[mid] > mid:
                high = mid - 1
            elif nums[mid] < mid:
                low = mid + 1

        return -1 if result == sys.maxsize else result


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve([-5, -2, 0, 3, 4]))
    print(solution.solve([-5, -4, 0]))
    print(solution.solve([0, 1, 2]))
