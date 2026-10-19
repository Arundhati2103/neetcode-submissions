class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted in increasing order
        # num1 + num2 = target and idx1 < idx2 
        i = 0
        j = len(numbers)-1

        while i<j:
            total = numbers[i] + numbers[j]

            if total == target:
                return [i+1, j+1]

            elif total > target:
                j -= 1

            else:
                i += 1
        
        
        