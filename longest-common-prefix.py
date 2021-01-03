from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        m = min(strs, key=lambda x: len(x))

        for index in range(len(m)):
            c = None

            for s in strs:
                if (c is not None) and s[index] != c:
                    return s[:index]
                c = s[index]

        return m


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["abc", "abcde"]))