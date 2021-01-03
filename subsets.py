from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        result = []
        for c in self.subsets(nums[1:]):
            result += [c, c + [nums[0]]]
        return result


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
