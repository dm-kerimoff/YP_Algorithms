mas = list(map(int, input().split()))

def even(mas):
    if ((mas[0] % 2 == 0) and (mas[1] % 2 == 0) and (mas[2] % 2 == 0)) or ((mas[0] % 2 != 0) and (mas[1] % 2 != 0) and (mas[2] % 2 != 0)):
        return 'WIN'
    else:
        return 'FAIL'

print(even(mas))
