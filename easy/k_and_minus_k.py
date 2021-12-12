# https://binarysearch.com/problems/K-and-K

class Solution:
    def solve(self, nums):
        s = set(nums)
        a = -1
        for num in nums:
            if -num in s:
                a = max(a, num)

        return a


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve([-4, 1, 8, -5, 4, -8]))
    print(solution.solve([5, 6, 1, -2]))
    print(solution.solve([1, 2, 0, 3, 4]))
