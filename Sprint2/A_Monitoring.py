n = int(input())
m = int(input())

a = [list(map(int,input().split())) for _ in range(n)]
result = [[None] * len(a) for _ in range(m)]

for i in range(m):
    for j in range(n):
        result[i][j] = a[j][i]

for item in result:
    row = item
    row = [str(elem) for elem in row]
    print(' '.join(row))