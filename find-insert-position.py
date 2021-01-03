from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index in range(len(nums)):
            if target <= nums[index]:
                return index

        return len(nums)