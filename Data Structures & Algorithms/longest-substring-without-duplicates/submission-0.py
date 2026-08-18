class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = 0
        substring = []
        for char in s:
            if char in substring:
                out = max(out, len(substring))
                substring = substring[substring.index(char) + 1:]
            substring.append(char)
        return max(out, len(substring))