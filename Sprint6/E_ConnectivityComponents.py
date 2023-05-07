from collections import defaultdict
import sys


def DFS(v, color, d, component_count):
    color[v-1] = component_count
    for w in sorted(d[v]):
        if color[w - 1] == -1:
            DFS(w, color, d, component_count)
    color[v-1] = component_count


def main():
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    d = defaultdict(list)
    for _ in range(m):
        data = list(map(int, input().split()))
        d[data[0]].append(data[1])
        d[data[1]].append(data[0])

    color = [-1] * n
    component_count = 1

    for i in range(1, n+1):
        if color[i-1] == -1:
            DFS(i, color, d, component_count)
            component_count += 1

    print(len(set(color)))
    for i in range(1, component_count+1):
        for j in range(1, n+1):
            if color[j-1] == i:
                print(j, end=' ')
        print()


if __name__ == '__main__':
    sys.setrecursionlimit(30000)
    main()

