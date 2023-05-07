from collections import defaultdict


def main():
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    d = defaultdict(list)
    for _ in range(m):
        data = list(map(int, input().split()))
        d[data[0]].append(data[1])

    print(d)

    for i in range(1, n+1):
        if len(d[i]) == 0:
            print(0)
        else:
            print(len(d[i]), *sorted(d[i]))


if __name__ == '__main__':
    main()