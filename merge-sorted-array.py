from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for index in range(0, n):
            nums1[m + index] = nums2[index]

        nums1.sort()


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [3, 4, 5]

    Solution().merge(nums1, 3, nums2, 3)

    print(nums1)
