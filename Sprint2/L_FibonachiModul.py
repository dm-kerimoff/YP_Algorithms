def FibHuf(n, k):
    d = 10 ** k
    if n < 2:
        return 1
    n -= 1
    l = [1, 1]
    for _ in range(n):
        s = (l[0] + l[1]) % d
        l[0] = l[1]
        l[1] = s
    return l[1]


n, k = (int(i) for i in input().split())
print(FibHuf(n, k))
