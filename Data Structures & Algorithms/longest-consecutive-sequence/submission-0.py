class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 1
        count = 1
        nums = sorted(set(nums))
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                count += 1
            else:
                count = 1
            res = max(res, count)
        return res
