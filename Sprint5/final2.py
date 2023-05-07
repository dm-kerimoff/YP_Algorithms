"""
id посылки: 80816949
1) Первый шаг — создание бинарной кучи. Сложность этой операции — O(1)
2) Далее вставим n элементов подряд в бинарную кучу:

Оценим сложность сверху:
O(log1)+O(log2)+...+O(logn) = O(logn)+O(logn)+...+O(logn)=O(n*logn)
3) Последним шагом извлекаем n элементов. Сложность этой операции также не больше, чем O(n*log n)

Получим:
T = O(1) + O(n*log n) + O(n*log n) = O(n*log n)
Это сложность алгоритма пирамидальной сортировки, которая в худшем случае работает не дольше, чем за O(n*logn)

Для описанной реализации алгоритма пирамидальной сортировки нужно выделить память под массив из n элементов.
То есть потребуется O(n) дополнительной памяти

"""
def heap_add(heap, key):
# Добавление в кучу элемента и выполнение просеивания вверх
    heap.append(key)
    sift_up(heap, len(heap)-1)


def sift_up(heap, idx):
# Просеивание вверх при добавлении элемента
    while idx > 1 and heap[idx] > heap[idx // 2]:
        heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
        idx = idx // 2


def heap_get_priority(heap):
    result = heap[1]
    heap[1] = heap[len(heap)-1]     # Вставка в итоговый массив приоритетного элемента
    heap.pop(-1)                    # Удаление элемента
    sift_down(heap, 1)              # Просеивание после удаления элемента
    return result


def sift_down(heap, idx):
# Выполнение просеивания вниз при удалении элемента
    left = 2 * idx
    right = 2 * idx + 1

    # нет дочерних узлов
    if len(heap) - 1 < left:
        return

    # right <= heap.size проверяет, что есть оба дочерних узла
    if right <= (len(heap) - 1) and heap[left] < heap[right]:
        idx_largest = right
    else:
        idx_largest = left

    if heap[idx] < heap[idx_largest]:
        heap[idx], heap[idx_largest] = heap[idx_largest], heap[idx]
        return sift_down(heap, idx_largest)
    else:
        return


def heapsort(array):
    # Создание пустой бинарной кучи
    heap = []
    for item in array:
        heap_add(heap, item)
    sorted_array = []
    while len(heap) > 1:
        sorted_array.append(heap_get_priority(heap))
    return sorted_array


def transform(members):
    """
    Функция возвращает список в формате [-1* очки, штраф, логин],
    удобный для сортировки и подготавливая этот список к быстрой сортировке
    """
    members[1] = -int(members[1])  # умножение на минус один необходимо, чтобы сортировать кол-во задач по возрастанию
    members[2] = int(members[2])
    return [members[1], members[2], members[0]]


def main():
    """
    Функция считывает количество участников number, создаёт список из списков members
    в формате, удобном для сортировки и выводит результат
    """
    number = int(input())
    members = [transform(input().split()) for _ in range(number)]
    members.insert(0, None)
    mas = heapsort(members)
    print(*(list(zip(*reversed(mas)))[2]), sep="\n")


if __name__ == '__main__':
    main()
