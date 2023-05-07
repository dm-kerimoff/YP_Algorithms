"""
74042690 - ID успешной посылки
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
    Сложность программы, выполняющая n команд равна O(n)

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Дек, максимальный размер которого определяется заданным числом m, занимает O(m) памяти.
"""


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
            self.back = (self.back + 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def push_front(self, value):
        if self.size != self.max_n:
            self.queue[self.front] = value
            self.front = (self.front - 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        fr_idx = (self.front + 1) % self.max_n
        x = self.queue[fr_idx]
        self.queue[fr_idx] = None
        self.front = fr_idx
        self.size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        bk_idx = (self.back - 1) % self.max_n
        x = self.queue[bk_idx]
        self.queue[bk_idx] = None
        self.back = bk_idx
        self.size -= 1
        return x


def main():

    n = int(input())
    max_size = int(input())
    d = Deque(max_size)
    commands = {
        'push_front': d.push_front,
        'push_back': d.push_back,
        'pop_front': d.pop_front,
        'pop_back': d.pop_back,
    }

    for _ in range(n):
        operation, *value = input().split()
        if value:
            try:
                if commands[operation](int(*value)) is not None:
                    print(commands[operation](int(*value)))
            except OverflowError:
                print('error')
        else:
            try:
                print(commands[operation]())
            except IndexError:
                print('error')


if __name__ == '__main__':
    main()
