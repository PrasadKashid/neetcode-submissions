class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for i in range(len(strs)):
            encoded += str(len(strs[i])) + "#" + strs[i]
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            # Skip '#'
            i += 1
            word = s[i : i + int(length)]
            result.append(word)
            # moving to the next string
            i += int(length)
        return result

