# ID 72133536
def near_zero(x, n):
    res = [0] * n  # заполним нулями итоговый массив
    ls_zero = -2 * n  # возьмём выходящее за границы массива отрицательное значение для прохода слева направо
    for i in range(len(x)):  # идём слева направо
        if x[i] != 0:
            res[i] = i - ls_zero
        else:
            ls_zero = i
    ls_zero = n ** 2  # возьмём выходящее за границы массива положительное значение для прохода справа налево
    for i in (range(len(x) - 1, -1, -1)):  # идём обратно справа налево
        if x[i] != 0:
            res[i] = min(ls_zero - i, res[i])
        else:
            ls_zero = i
    return ' '.join(list(map(str, res)))


def main():
    n = int(input())
    x = [int(i) for i in input().split()]
    print(near_zero(x, n))


if __name__ == '__main__':
    main()
