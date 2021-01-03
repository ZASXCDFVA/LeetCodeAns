from typing import List


class MinStack:
    def __init__(self):
        self._stack: List[int] = []
        self._sorted: List[int] = []

    def push(self, x: int) -> None:
        self._stack.append(x)
        self._sorted = sorted(self._stack)

    def pop(self) -> None:
        self._stack.pop()
        self._sorted = sorted(self._stack)

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._sorted[0]

