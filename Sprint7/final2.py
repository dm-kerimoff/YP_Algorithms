"""
id посылки - 84759796

Идея алгоритма позаимствована с сайта wikipedia - Задача разбиения множества чисел

Временная сложность - O(n*S), где n - кол-во элементов массива, S - сумма элементов
Пространственная сложность - O(S)

"""


def equal_sums(points):
    s = sum(points)
    if s % 2 != 0:
        return False    # Если сумма нечётна - то последовательность нельзя разделить на две подпосл-сти равной суммы
    s_half = s // 2
    dp = [True] + [False] * s_half
    for point in points:
        for j in range(s_half, point - 1, -1):
            dp[j] = dp[j - point] or dp[j]
            if j == s_half and dp[j]:
                return True
    return dp[-1]


def main():
    _ = int(input())
    print(equal_sums(list(map(int, input().split()))))


if __name__ == '__main__':
    main()
