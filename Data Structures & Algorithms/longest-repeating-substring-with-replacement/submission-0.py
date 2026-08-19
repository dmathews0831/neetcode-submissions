class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0
        left = 0
        most_freq = 0
        
        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            most_freq = max(most_freq, count[char])

            while (right - left + 1) - most_freq > k:
                count[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)

        return longest
