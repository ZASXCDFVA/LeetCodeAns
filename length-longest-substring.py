class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index: int = 0

        longest: int = 0

        while index < len(s):
            offset: int = 0
            existed: int = 0

            while (index + offset) < len(s):
                new_existed = existed | (1 << (ord(s[index + offset]) - 33))

                if new_existed == existed:
                    break

                offset += 1
                existed = new_existed

            if offset > longest:
                longest = offset

            index += 1

        return longest


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(""))
