class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        print(self.queue[self.head])


n = int(input())
max_size = int(input())
q = MyQueueSized(max_size)
for _ in range(n):
    elem = input()
    if elem == 'peek':
        if q.is_empty():
            print('None')
        else:
            q.peek()
    elif elem == 'size':
        print(q.size)
    elif elem == 'pop':
        print(q.pop())
    else:
        if q.size == q.max_n:
            print('error')
        else:
            l = elem.split()
            q.push(int(l[1]))
