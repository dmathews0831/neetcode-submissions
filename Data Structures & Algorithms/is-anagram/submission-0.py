class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Schars = set(list(s))
        Tchars = set(list(t))
        if Schars != Tchars:
            return False
        for char in Schars:
            if s.count(char) != t.count(char):
                return False
        return True