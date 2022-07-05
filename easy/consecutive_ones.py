# https://binarysearch.com/problems/Consecutive-Ones

class Solution:
    def solve(self, nums):
        # 0 - not found
        # 1 - found
        # 2 - not consecutively
        result = 0

        for i in nums:
            if i == 1 and result == 0:
                result = 1
            elif i == 1 and result == 2:
                return False
            if i != 1 and result == 1:
                result = 2
        return True