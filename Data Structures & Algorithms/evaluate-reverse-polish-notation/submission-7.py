class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = '+-*/'
        for tok in tokens:
            if tok in ops:
                a = stack.pop()
                b = stack.pop()
                if tok == '+':
                    stack.append(a + b)
                elif tok == '-':
                    stack.append(b - a)
                elif tok == '*':
                    stack.append(a * b)
                elif tok == '/':
                    stack.append(int(b / a))
            else:
                stack.append(int(tok))
        return stack[0]
