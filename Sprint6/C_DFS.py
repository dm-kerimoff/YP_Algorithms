from collections import defaultdict


class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, val):
        self.items.append(val)

    def IsEmpty(self):
        return len(self.items) == 0


def DFS(v, visit, d):
    s = Stack()
    s.push(v)
    while not s.IsEmpty():
        w = s.pop()
        if not visit[w-1]:
            print(w)
            visit[w-1] = True

        for i in d[w]:
            if not visit[i-1]:
                s.push(i)


def main():
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    d = defaultdict(list)
    for _ in range(m):
        data = list(map(int, input().split()))
        d[data[0]].append(data[1])
        d[data[1]].append(data[0])

    visit = [False]*n
    for i in d:
        d[i]=sorted(d[i], reverse=True)

    DFS(int(input()), visit, d)


if __name__ == '__main__':
    main()