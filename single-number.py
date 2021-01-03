from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if (i - 1 < 0 or nums[i - 1] != nums[i]) and (i >= len(nums) - 1 or nums[i + 1] != nums[i]):
                return nums[i]

        return nums[0]


if __name__ == '__main__':
    print(Solution().singleNumber([1, 1]))
