# https://binarysearch.com/problems/Stuck-Keyboard

class Solution:
    def counter(self, s):
        result = []
        current = s[0]
        counter = 0

        for i in range(len(s)):
            if s[i] == current:
                counter += 1
            else:
                result.append({current: counter})
                counter = 1
                current = s[i]
        result.append({current: counter})
        return result

    def solve(self, typed, target):
        if typed == target:
            return True
        if len(typed) == 0 and len(target) != 0 or len(typed) != 0 and len(target) == 0:
            return False
        if len(typed) < len(target):
            return False

        target_result = self.counter(target)
        typed_result = self.counter(typed)

        for i in target_result:
            if len(typed_result) == 0:
                return False
            if list(i.keys())[0] in typed_result[0] and list(i.items())[0][1] <= list(typed_result[0].items())[0][1]:
                typed_result.pop(0)
            else:
                return False
        return len(typed_result) == 0


if __name__ == '__main__':
    solution = Solution()
    # print(solution.solve('bb', 'ba'))
    # print(solution.solve('aaa', 'aa'))
    print(solution.solve('acc', 'aac'))
