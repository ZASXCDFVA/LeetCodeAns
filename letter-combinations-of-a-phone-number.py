from typing import List


class Solution:
    def __init__(self):
        self._map_of = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def _append(self, result: List[str], prefix: str, current: str):
        if current == "":
            if prefix != "":
                result.append(prefix)
            return

        for c in self._map_of[int(current[0]) - 2]:
            self._append(result, prefix + c, current[1:])

    def letterCombinations(self, digits: str) -> List[str]:
        result: List[str] = []

        self._append(result, "", digits)

        return list(result)


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
