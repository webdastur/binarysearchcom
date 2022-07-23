# https://binarysearch.com/problems/Buying-Cars

class Solution:
    def solve(self, prices, k):
        prices.sort()

        count = 0

        for i in prices:
            if k - i >= 0:
                k -= i
                count += 1
            else:
                break
        return count
