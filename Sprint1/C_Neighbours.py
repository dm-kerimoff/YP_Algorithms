def neighbs(mx,k,l):
    res = []
    #От нашего элемента слева и справа должен быть запас в один элемент
    if l + 1 < len(mx[0]):
        res.append(mx[k][l+1])
    if l - 1 >= 0:
        res.append(mx[k][l-1])
    if k + 1 < len(mx):
        res.append(mx[k+1][l])
    if k-1 >= 0:
        res.append(mx[k-1][l])
    res.sort()
    res = [str(i) for i in res]
    return res

n = int(input())
m = int(input())
mx = [list(map(int, input().split())) for i in range(n)]
# Координаты элемента
k = int(input())
l = int(input())

print(' '.join(neighbs(mx,k,l)))
