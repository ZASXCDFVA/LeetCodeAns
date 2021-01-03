class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        e = -1
        c = 0

        for n in nums:
            if e == n:
                c += 1
                if c >= len(nums) // 2:
                    return e
            else:
                c = 0

            e = n

        return e
