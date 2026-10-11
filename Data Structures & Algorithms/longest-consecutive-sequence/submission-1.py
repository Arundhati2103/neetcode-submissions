class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # optimal solution using hashset
        hashset = set(nums)
        res = 0
        for num in hashset:
            if num-1 not in hashset:
                count = 1
                while num + count in hashset:
                    count += 1
                res = max(res, count)
        return res
