def two(n):
    res = []
    while n != 0:
        res.append(n % 2)
        n = n // 2
    res = [str(i) for i in res]
    res = res[::-1]

    return ''.join(res)


n = int(input())
if n == 0:
    print('0')
else:
    print(two(n))
