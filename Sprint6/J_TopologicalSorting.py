from collections import defaultdict
import sys


class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, val):
        self.items.append(val)

    def IsEmpty(self):
        return len(self.items) == 0


def TopSort(v, color, d, order):
    color[v-1] = 'gray'
    for w in sorted(d[v]):
        if color[w - 1] == 'white':
            TopSort(w, color, d, order)
    color[v-1] = 'black'
    order.push(v)


def main():
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    d = defaultdict(list)
    for _ in range(m):
        data = list(map(int, input().split()))
        d[data[0]].append(data[1])

    color = ['white'] * n
    order = Stack()

    for i in range(1, n+1):
        if color[i-1] == 'white':
            TopSort(i, color, d, order)
    print(*order.items[::-1])


if __name__ == '__main__':
    sys.setrecursionlimit(30000)
    main()

