class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & 1
        n = n >> 1

        while n:
            if n & 1 != prev:
                prev = n & 1
                n = n >> 1
            else:
                return False

        return True


if __name__ == '__main__':
    print(Solution().hasAlternatingBits(7))
