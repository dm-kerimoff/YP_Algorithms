def fun(m):
    return m[0]*m[1]**2 + m[2]*m[1] + m[3]

m = list(map(int, input().split()))
print(fun(m))
