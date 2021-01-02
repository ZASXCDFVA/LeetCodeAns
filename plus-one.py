from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value = int("".join(map(lambda x: str(x), digits)))

        if value == 0:
            digits[-1] = 1

            return digits

        return list(map(lambda x: int(x), str(value + 1)))


if __name__ == '__main__':
    print(Solution().plusOne([0, 0, 0]))
