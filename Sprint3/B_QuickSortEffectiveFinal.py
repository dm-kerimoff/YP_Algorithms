# 76152021
"""
Временная сложность:
    Лучший случай - О(n) * O(log n) = О(n * log n)
    Среднее - О(n * log n)
    Худший случай - О(n) * O(n) = О(n^2)

Пространственная сложность:
    Требует лишь O(1) дополнительной памяти для своей работы.
"""


def partition(members, left, right):
    """Модификация, основанная на in-place """
    pivot = members[left]
    i = left + 1    # левый указатель
    j = right - 1   # правый указатель
    while True:
        if i <= j and members[j] > pivot:
            j -= 1                          #сдвиг правого указателя
        elif i <= j and members[i] < pivot:
            i += 1                          #сдвиг левого указателя
        elif (members[j] > pivot) or (members[i] < pivot):
            continue
        if i <= j:
            members[i], members[j] = members[j], members[i]         #swap элементов, на которые указывают указатели
        else:
            members[left], members[j] = members[j], members[left]
            return j


def quick_sort(members, left, right):
    if (right - left) > 1:
        p = partition(members, left, right)
        quick_sort(members, left, p)        # сортировка левого подмассива
        quick_sort(members, p + 1, right)   # сортировка правого подмассива


def transform(members):
    """
    Функция возвращает список в формате [-1* очки, штраф, логин],
    удобный для сортировки и подготавливая этот список к быстрой сортировке
    """
    members[1] = - int(members[1])  # умножение на минус один необходимо, чтобы сортировать кол-во задач по возрастанию
    members[2] = int(members[2])
    return [members[1], members[2], members[0]]


def main():
    """
    Функция считывает количество участников number, создаёт список из списков members
    в формате, удобном для сортировки, выполняет сортировку in-place и выводит результат
    """
    number = int(input())
    members = [transform(input().split()) for _ in range(number)]
    left = 0
    quick_sort(members, left, len(members))         #указатели left и right изначально на левый и правый концы массива
    print(*(list(zip(*members))[2]), sep = "\n")


if __name__ == '__main__':
    main()
