class MinStack:

    def __init__(self):
        self.stack = []
        self.low = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.low:
            self.low.append(min(val,self.low[-1]))
        else:
            self.low.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.low.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.low[-1]
