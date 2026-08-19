class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = sorted(s1)
        length = len(perm)
        l, r = 0, length
        while r <= len(s2):
            if sorted(s2[l:r]) == perm:
                return True
            else:
                r += 1
                l += 1
            
        return False

