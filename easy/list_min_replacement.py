# https://binarysearch.com/problems/List-Min-Replacement

class Solution:
    def solve(self, nums):
        min_item = nums[0]

        nums[0] = 0

        if len(nums) == 1:
            return nums

        for i in range(1, len(nums)):
            current = nums[i]
            nums[i] = min_item
            min_item = min(current, min_item)
        return nums
