from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        bits: int = 0

        for n in nums:
            bits |= 1 << n

        index = 0

        bits = ~bits

        while bits != 0:
            if bits & 0xFFFFFFFF != 0:
                break

            index += 32
            bits >>= 32

        bits = bits & 0xFFFFFFFF

        while bits & 1 == 0:
            bits >>= 1
            index += 1

        return index


if __name__ == '__main__':
    print(Solution().missingNumber([3, 0, 1]))
