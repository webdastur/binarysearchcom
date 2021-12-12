# https://binarysearch.com/problems/Win-After-Last-Round


from typing import List


class Solution:
    def solve(self, nums: List[int]):
        nums.sort(reverse=True)
        try:
            cut = max(num + i for i, num in enumerate(nums, 1))
        except ValueError:
            return 0
        for i, num in enumerate(nums):
            if num + len(nums) < cut:
                return i
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.solve([8, 7, 10, 11]))
    print(solution.solve([10, 8, 7]))
