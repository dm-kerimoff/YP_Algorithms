# 77691037
"""
    Структура абстрактного типа данных - коллекция соответствий между ключами и значениями.
    Все ключи уникальны.

    Мы используем два списка, чтобы создать класс HashTable
    Один список, называемый keys, будет содержать ключи элементов,второй список - список values - значения данных.
    Если мы находим ключ, на соответствующей позиции в списке с данными будет находиться соответствующее с ним значение.

    Для разрешения коллизий используется метод открытой адресации

    Сложность(временная)
    Поиск элемента - O(1) - константное время, в худшем случае - O(n)
    Все операции выполняются за O(1) в среднем: то есть если n операций, то n запросов выполняются за O(n)

    Сложность(пространственная):
    O(1) - константная сложность(при создании таблицы с дефолтным значением корзин)
"""


class HashTable:
    def __init__(self, size=int(10**5 * 4/3)+4):
        """
        Атрибуты: размер таблицы size(size = простое число,близкое к 10^5 * 4/3), список ключей и список значений соответственно
        """
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def put(self, key, value):
        """
        Вычисляем хэш-значение и, если ячейка не пуста, применяем функцию next_pos до тех пор,
        пока не найдём свободное место для вставки.
        Если непустая ячейка уже содержит ключ, заменяем старое значение новым.
        """
        unit = self.hash(key)
        if self.keys[unit] is None:
            self.keys[unit] = key
            self.values[unit] = value
        elif self.keys[unit] == key:
            self.values[unit] = value
        else:
            next_unit = self.find_pos(self.next_pos(unit), key)

            if self.keys[next_unit] is None:
                self.keys[next_unit] = key
            self.values[next_unit] = value

    def hash(self, key):
        """
        Хеш функция реализуется методом простых остатков
        Равные числовые значения имеют одинаковое значение хеш-функции, даже если они имеют разные типы
        """
        return hash(key) % self.size

    def next_pos(self, prev_hash):
        """
        Функция rehash определяет следующую позицию
        """
        return hash(prev_hash + 1) % self.size

    def find_pos(self, pos, key):
        while self.keys[pos] is not None and self.keys[pos] != key:
            pos = self.next_pos(pos)
        return pos

    def get(self, key):
        """
        Получение значения по ключу key
        """
        pos = self.find_pos(self.hash(key), key)
        return self.values[pos] if self.keys[pos] == key else None

    def delete(self, key):
        """
        Удаление элемента по его ключу
        Если по данному ключу лежит значение None, то мы его и возвращаем
        """
        data = self.get(key)
        if data is not None:
            self.put(key, None)
        return data


def main():
    n = int(input())
    hashtable = HashTable()
    for _ in range(n):
        command = input().split()
        if len(command) == 2:
            print(getattr(hashtable, command[0])(int(command[1])))
        else:
            getattr(hashtable, command[0])(*map(int, command[1:]))


if __name__ == '__main__':
    main()
