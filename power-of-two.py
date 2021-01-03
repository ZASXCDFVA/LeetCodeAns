from typing import Set


class Solution:
    def __init__(self):
        self._dict: Set[int] = set()

        value = 1

        for i in range(32):
            self._dict.add(value)

            value <<= 1

    def isPowerOfTwo(self, n: int) -> bool:
        return n in self._dict


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(6))
