def fun(n, mas):
    sum = 0
    for i in range(n):
        if (i == 0 or mas[i] > mas[i-1]) and (i == n - 1 or mas[i] > mas[i+1]):
            sum += 1
    return sum

n = int(input())
mas = list(map(int, input().split()))
print(fun(n, mas))
