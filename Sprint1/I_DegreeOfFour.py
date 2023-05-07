def is_four(n):
    while n != 1:
        if n % 4 != 0:
            return False
        else:
            n = n // 4
    return True

n = int(input())
print(is_four(n))
