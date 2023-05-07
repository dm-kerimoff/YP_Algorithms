# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень
    if l < n and arr[i] < arr[l]:
        largest = l
    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)


# Основная функция для сортировки массива заданного размера
def heapSort(arr):
    n = len(arr)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] #
        heapify(arr, i, 0)


def transform(members):
    """
    Функция возвращает список в формате [-1* очки, штраф, логин],
    удобный для сортировки и подготавливая этот список к быстрой сортировке
    """
    members[1] = - int(members[1])  # умножение на минус один необходимо, чтобы сортировать кол-во задач по возрастанию
    members[2] = int(members[2])
    return [members[1], members[2], members[0]]


# Управляющий код для тестирования
number = int(input())
arr = [transform(input().split()) for _ in range(number)]
heapSort(arr)
n = len(arr)
print(*(list(zip(*arr))[2]), sep = "\n")