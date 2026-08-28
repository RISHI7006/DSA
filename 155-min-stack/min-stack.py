class MinStack:
    def __init__(self):
        self.stack = []       # holds all values
        self.min_stack = []   # tracks minimum at each level

    def push(self, val: int) -> None:
        self.stack.append(val)

        # Push to min_stack: either val itself (new minimum) 
        # or the current minimum (if val isn't smaller)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]