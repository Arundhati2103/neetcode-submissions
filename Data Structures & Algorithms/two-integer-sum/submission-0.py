class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target is 7 -> [0,1] why? 3+4
        # nums[i] + target - nums[i] = target

        hashmap = {}

        for idx, num in enumerate(nums):
            diff = target - nums[idx]
            if diff in hashmap:
                return [hashmap[diff], idx]
            hashmap[num] = idx
        
        