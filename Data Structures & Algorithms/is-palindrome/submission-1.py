class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using list instead of string
        res = []
        for word in s:
            if word.isalnum():
                res.append(word.lower())
        res = ''.join(res)
        return res==res[::-1]        