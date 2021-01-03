import random


def rand7() -> int:
    return random.randint(0, 7)


class Solution:
    def __init__(self):
        self._elements = []

    def rand10(self) -> int:
        if len(self._elements) == 0:
            self._elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

            for a in range(10):
                b = (rand7() + rand7()) % 10

                self._elements[a], self._elements[b] = self._elements[b], self._elements[a]

        return self._elements.pop()


if __name__ == '__main__':
    s = Solution()

    print("".join((str(s.rand10()) for _ in range(100))))
