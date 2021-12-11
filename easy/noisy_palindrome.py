# https://binarysearch.com/problems/Noisy-Palindrome

class Solution:
    def solve(self, s: str) -> bool:
        cleaned_str = "".join([i for i in s if i.islower()])
        return cleaned_str == cleaned_str[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve("a92bcbXa"))
