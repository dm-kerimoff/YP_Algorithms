from collections import defaultdict


def main():
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    d = defaultdict(list)
    for _ in range(m):
        data = list(map(int, input().split()))
        d[data[0]].append(data[1])

    mx = [[0]*n for _ in range(n)]
    for i in d:
        for j in d[i]:
            mx[i-1][j-1] = 1

    for i in mx:
        print(*i)


if __name__ == '__main__':
    main()