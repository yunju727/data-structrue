class Queue:
    MAX_QSIZE = 10

    def __init__(self):
        self.items = [None]*self.MAX_QSIZE
        self.front = 0
        self.rear = 0
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, e):
        if self.size == len(self.items):
            self.resize(2*len(self.items))
            self.items[self.rear] = e
            self.rear = (self.rear+1) % (len(self.items))
            self.size += 1
        else:
            self.items[self.rear] = e
            self.rear = (self.rear+1) % (len(self.items))
            self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return False
        else:
            e = self.items[self.front]
            self.front = (self.front+1) % (len(self.items))
            self.size -= 1
            return e

    def resize(self, cap):
        olditems = self.items
        self.items = [None]*cap
        walk = self.front
        for k in range(self.size):
            self.items[k] = olditems[walk]
            walk = (walk+1) % len(olditems)
        self.front = 0
        self.rear = self.size

    def __len__(self):
        return self.size


line = Queue()
n = int(input())
for i in range(n):
    line.enqueue(list(map(int, input().split())))
pre_waiting = 0
cur_waiting = 0
total_waiting = 0
sangdam = 0
if len(line) == 0:
    print("%0.2f" % 0.00)
else:
    for i in range(len(line)):
        a = line.dequeue()
        if i == 0:
            cur_waiting = 0
        else:
            pre_waiting = cur_waiting
            cur_waiting = pre_waiting-a[0]+sangdam
            if cur_waiting < 0:
                cur_waiting = 0
        sangdam = a[1]
        total_waiting += cur_waiting

    print("%0.2f" % (total_waiting/n))
