"""
id посылки - 84991964
Идея для решения задачи и дополнительная теория взяты с https://habr.com/ru/post/676858/

Временная сложность - O(m*n), где m,n - длины строк

Пространственная сложность:  O(n), где n - длина наименьшей строки.

"""


def levenshtein_distance(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2, n, m = str_2, str_1, m, n

    current = list(range(n + 1))
    for i in range(1, m + 1):
        prev, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            current[j] = min(
                prev[j] + 1,
                current[j - 1] + 1,
                prev[j - 1] + 1 if str_1[j - 1] != str_2[i - 1] else prev[j - 1]
            )
    return current[n]


def main():
    str_1, str_2 = input(), input()
    print(levenshtein_distance(str_1, str_2))


if __name__ == '__main__':
    main()
