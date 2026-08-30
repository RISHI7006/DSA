class MyCircularQueue {
private:
    vector<int> queue;
    int capacity;
    int frontIdx;
    int size;

public:
    MyCircularQueue(int k) {
        capacity = k;
        queue.resize(k);
        frontIdx = 0;
        size = 0;
    }

    bool enQueue(int value) {
        if (isFull()) return false;

        int rearIdx = (frontIdx + size) % capacity;
        queue[rearIdx] = value;
        size++;
        return true;
    }

    bool deQueue() {
        if (isEmpty()) return false;

        frontIdx = (frontIdx + 1) % capacity;
        size--;
        return true;
    }

    int Front() {
        if (isEmpty()) return -1;
        return queue[frontIdx];
    }

    int Rear() {
        if (isEmpty()) return -1;
        int rearIdx = (frontIdx + size - 1) % capacity;
        return queue[rearIdx];
    }

    bool isEmpty() {
        return size == 0;
    }

    bool isFull() {
        return size == capacity;
    }
};