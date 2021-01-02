class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        try:
            return len(list(filter(lambda x: len(x) > 0, s.split(" ")))[-1])
        except:
            return 0


if __name__ == '__main__':
    print(Solution().lengthOfLastWord(""))
