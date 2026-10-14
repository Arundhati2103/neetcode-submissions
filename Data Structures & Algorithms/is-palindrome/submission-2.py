class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using two pointers to reduce space complexity from O(N) to O(1)
        left = 0
        right = len(s)-1

        while left < right:
            if not s[left].isalnum():
                left += 1

            elif not s[right].isalnum():
                right -= 1

            elif s[left].lower() != s[right].lower():
                return False # since its case sensitive
            
            else:
                left += 1
                right -= 1
        return True

            

        