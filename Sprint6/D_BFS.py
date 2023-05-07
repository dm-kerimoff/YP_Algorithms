from collections import defaultdict


class Queue:
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


def BFS(s, d, n, color):
    planned = Queue(n)
    planned.push(s)
    color[s-1] = 'gray'


    while planned.is_empty() is False:
        u = planned.pop()
        print(u, end=' ')
        for v in sorted(d[u]):
            if color[v-1] == 'white':
                color[v-1] = 'gray'
                planned.push(v)
        color[u-1] = 'black'


def main():
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    d = defaultdict(list)
    for _ in range(m):
        data = list(map(int, input().split()))
        d[data[0]].append(data[1])
        d[data[1]].append(data[0])

    color = ['white'] * n

    BFS(int(input()), d, n, color)


if __name__ == '__main__':
    main()