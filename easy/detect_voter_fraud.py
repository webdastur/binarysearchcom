# https://binarysearch.com/problems/Detect-Voter-Fraud

class Solution:
    def solve(self, votes):
        cache = set()

        for i in votes:
            if i[1] in cache:
                return True
            else:
                cache.add(i[1])
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve([
        [3, 1],
        [3, 0],
        [3, 4],
        [3, 3],
        [3, 2]
    ]))
    print(solution.solve([
        [2, 3],
        [2, 2],
        [2, 1],
        [2, 0],
        [2, 1]
    ]))
