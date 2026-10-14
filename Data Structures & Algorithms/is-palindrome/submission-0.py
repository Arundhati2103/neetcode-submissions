class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for word in s:
            if word.isalnum():
                res += word.lower()
        return res==res[::-1]       