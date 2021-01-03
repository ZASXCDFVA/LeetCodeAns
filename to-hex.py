class Solution:
    def __init__(self):
        self._map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

    def toHex(self, num: int) -> str:
        r = []

        if num < 0:
            num = num + 0x100000000
        elif num == 0:
            return "0"

        while num:
            r.append(self._map[num & 0xF])

            num >>= 4

        r.reverse()

        return "".join(r)


if __name__ == '__main__':
    print(Solution().toHex(-1))
