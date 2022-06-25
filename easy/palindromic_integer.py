# https://binarysearch.com/problems/Palindromic-Integer

class Solution:
    def solve(self, num):
        after, current = 0, num
        while num > 0:
            right = num % 10
            num = num // 10
            after = (10 * after) + right
        return after == current
