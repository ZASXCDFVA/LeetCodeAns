from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum: int = nums[i] + nums[j]

                if sum == target:
                    return [i, j]


if __name__ == '__main__':
    print(Solution().twoSum([3, 2, 4], 6))
