class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0

        while n != 0:
            if n & 0xFFFF == 0:
                n >>= 16
                continue

            if n & 1 != 0:
                c += 1

            n >>= 1

        return c
