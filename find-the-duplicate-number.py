from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return nums[i]

        return nums[0]


if __name__ == '__main__':
    print(Solution().findDuplicate([1, 3, 4, 2, 2]))
