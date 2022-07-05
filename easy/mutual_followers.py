# https://binarysearch.com/problems/Mutual-Followers

class Solution:
    def solve(self, relations):
        seen = set()
        ans = set()

        for a, b in relations:
            seen.add((a, b))

            if (b, a) in seen:
                ans.add(a)
                ans.add(b)

        return sorted(list(ans))