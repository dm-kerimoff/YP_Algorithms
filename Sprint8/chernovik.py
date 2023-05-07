"""
id посылки - 86273925

Этапы решения задачи:
а) Распаковка каждой строки
б) Поиск наибольшего общего префикса(берём 2 строки, ищем общий префикс, результат улучшаем третьей строкой и т.д)

Временная сложность:
    O(n*m), где n - количество строк, m - длина наибольшей строки

Пространственная сложность:
    O(m), где m - длина наибольшей строки
"""


def decompress(string):
    stack = []
    letters = []
    for i in string:
        if i != ']':
            stack.append(i)
        else:
            letter = stack.pop()
            while letter != '[':
                letters.append(letter)
                letter = stack.pop()

            word = ''.join(letters[::-1])
            letters = []

            stack.append(''.join([word for _ in range(int(stack.pop()))]))

    return list(''.join(stack))


def max_prefix(n):
    if n == 0:
        return ''
    prefix = decompress(input())
    for _ in range(n - 1):
        string = decompress(input())
        while string[:len(prefix)] != prefix and prefix:
            prefix.pop()
    return ''.join(prefix)


def main():
    n = int(input())
    print(max_prefix(n))


if __name__ == "__main__":
    main()
