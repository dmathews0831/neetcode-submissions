class Solution:
    def isValid(self, s: str) -> bool:
        options = {"{":"}", "[":"]", "(":")"}
        stack = []
        for char in s:
            if char in options:
                stack.append(char)
                continue
            elif stack:
                if options[stack[-1]] == char:
                    stack.pop()
                    continue
            return False
        return not stack