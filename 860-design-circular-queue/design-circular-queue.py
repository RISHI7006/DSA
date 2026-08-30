class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.queue = [0] * k
        self.front_idx = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        # Calculate the position to insert (wraps around using modulo)
        rear_idx = (self.front_idx + self.size) % self.capacity
        self.queue[rear_idx] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        # Move front pointer forward, wrapping around if needed
        self.front_idx = (self.front_idx + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front_idx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        rear_idx = (self.front_idx + self.size - 1) % self.capacity
        return self.queue[rear_idx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity