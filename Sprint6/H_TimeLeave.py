from collections import defaultdict
import sys


def DFS(v, color, d, time, entry, leave):
    entry[v - 1] = time[0]
    time[0] += 1
    color[v-1] = 'gray'
    for w in sorted(d[v]):
        if color[w - 1] == 'white':
            DFS(w, color, d, time, entry, leave)
    leave[v-1] = time[0]
    time[0] += 1
    color[v-1] = 'black'


def main():
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    d = defaultdict(list)
    for _ in range(m):
        data = list(map(int, input().split()))
        d[data[0]].append(data[1])

    color = ['white'] * n
    time = [0]
    entry = [None] * n
    leave = [None] * n
    DFS(1, color, d, time, entry, leave)

    for i in range(n):
        print(entry[i], leave[i])


if __name__ == '__main__':
    sys.setrecursionlimit(30000)
    main()

