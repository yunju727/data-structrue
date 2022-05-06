class Queue:
    MAX_QSIZE = 5

    def __init__(self):
        self.item = [None]*Queue.MAX_QSIZE
        self.size = 0
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, x):
        if self.size == len(self.items):
            self.resize(2*len(self.items))
        self.rear = (self.rear+1) % len(self.items)
        self.items[self.rear] = x
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return False
        else:
            self.front = (self.front+1) % len(self.items)
            e = self.items[self.front]
            self.size -= 1
            return e

    def resize(self, cap):
        olditem = self.items
        self.items = [None]*cap
        walk = self.front
        for i in range(len(olditem)):
            self.items[i] = olditem[walk]
            walk = (walk+1) % len(olditem)
        self.front = -1
        self.rear = self.size-1
