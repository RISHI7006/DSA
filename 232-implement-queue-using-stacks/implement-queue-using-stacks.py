class MyQueue:
    def __init__(self):
        self.stack_in = []   # for pushing new elements
        self.stack_out = []  # for popping/peeking (reversed order)

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self._transfer_if_needed()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._transfer_if_needed()
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

    def _transfer_if_needed(self) -> None:
        # Only transfer when stack_out is empty
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())