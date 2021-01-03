def isBadVersion(version: int) -> bool:
    return version > 10


class Solution:
    def firstBadVersion(self, n: int) -> int:
        for i in range(1, n + 1):
            if isBadVersion(i):
                return i
