class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + '#' + s
        return res



    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):
            j = i

        # Find the end of the length prefix
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

        # Read exactly 'length' characters
            start = j + 1
            end = start + length

            result.append(s[start:end])

        # Move to the next encoded string
            i = end
        return result
