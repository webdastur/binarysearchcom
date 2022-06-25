# https://binarysearch.com/problems/Wolf-of-Wall-Street

class Solution:
    def solve(self, prices):
        if len(prices) == 0:
            return 0
        max_index = 0
        min_index = prices[0]
        for i in prices:
            min_index = min(min_index, i)
            max_index = max(max_index, i - min_index)
        return max_index


if __name__ == '__main__':
    solution = Solution()
    # print(solution.solve([9, 11, 8, 5, 7, 10]))
    # print(solution.solve([1, 1]))
    print(solution.solve([0, 1]))
