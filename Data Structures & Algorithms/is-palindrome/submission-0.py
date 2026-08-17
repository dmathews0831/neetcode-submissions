class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(filter(str.isalnum, s)).lower()
        for i in range(len(cleaned)//2):
            if cleaned[i] != cleaned[-(1+i)]:
                return False
        return True