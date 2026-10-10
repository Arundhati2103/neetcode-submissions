class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # i/p = [1, 2, 4, 6]

        # o/p = [2x4x6, 1x4x6, 1x2x6, 1x2x4]
        # to avoid same operation at multiple steps is there a way we could calcualte the res at the left index everytime we move forward
        # once we are done with left prefix, we need right suffix

        # answer[i] = prefix[i] x suffix[i]

        # calculate prefix first
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        res = [1]*n
        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res

        