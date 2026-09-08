class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = str(digits).replace(", ","").strip()[1:-1]
        num = int(s) + 1
        return list(str(num))