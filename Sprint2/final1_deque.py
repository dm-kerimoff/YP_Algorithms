"""
73927530 - ID успешной посылки
ПРИНЦИП РАБОТЫ
    Дек, максимальный размер которого определяется заданным числом.
ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
    Структура, объединяющая стек и очередь, называется дек
    Она поддерживает набор операций:
    - Добавить элемент в начало дека;
    - Извлечь элемент из начала дека;
    - Добавить элемент в конец дека;
    - Извлечь элемент из конца дека;
    - Проверить, пуст ли дек;

ВРЕМЕННАЯ СЛОЖНОСТЬ
    Добавление в дек занимает O(1).
    Извлечение из дека занимает O(1).
    Проверить, пуст ли дек занимает O(1).
    Проверить, полон ли дек занимает O(1).

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Дек, максимальный размер которого определяется заданным числом m, занимает O(m) памяти.
"""


def main():
    class Deque:
        def __init__(self, n):
            self.queue = [None] * n
            self.max_n = n
            self.front = -1
            self.back = 0
            self.size = 0

        def is_empty(self):
            return self.size == 0

        def size(self):
            return self.size

        def push_back(self, value):
            if self.size != self.max_n:
                self.queue[self.back] = value
                self.back = check_mod(self.back + 1, self.max_n)
                self.size += 1
            else:
                print('error')

        def push_front(self, value):
            if self.size != self.max_n:
                self.queue[self.front] = value
                self.front = check_mod(self.front - 1, self.max_n)
                self.size += 1
            else:
                print('error')

        def pop_front(self):
            if self.is_empty():
                return 'error'
            fr_idx = check_mod(self.front + 1, self.max_n)
            x = self.queue[fr_idx]
            self.queue[fr_idx] = None
            self.front = fr_idx
            self.size -= 1
            return x

        def pop_back(self):
            if self.is_empty():
                return 'error'
            bk_idx = check_mod(self.back - 1, self.max_n)
            x = self.queue[bk_idx]
            self.queue[bk_idx] = None
            self.back = bk_idx
            self.size -= 1
            return x

    def check_mod(idx, size):
        return idx % size if idx >= 0 else idx % (-size)

    n = int(input())
    max_size = int(input())
    d = Deque(max_size)

    for _ in range(n):
        elem = input()
        if elem == 'pop_back':
            print(d.pop_back())
        elif elem == 'pop_front':
            print(d.pop_front())
        elif elem.split()[0] == 'push_back':
            d_elem = int(elem.split()[-1])
            d.push_back(d_elem)
        else:
            d_elem = int(elem.split()[-1])
            d.push_front(d_elem)


if __name__ == '__main__':
    main()
