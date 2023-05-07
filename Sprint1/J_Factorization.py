def razlozh(n):
    i = 2
    res = []
    while (i*i <= n):
        if (n % i == 0):
            res.append(i)
            n = n // i
        else:
            i += 1
    if n != 1:
        res.append(n)

    res = [str(i) for i in res]
    return ' '.join(res)

n = int(input())
print(razlozh(n))
        
