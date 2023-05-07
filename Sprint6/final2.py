"""
По опредению имеем:
Карта железных дорог называется оптимальной, если не существует пары городов A и B такой,
что от A до B можно добраться как по дорогам типа R, так и по дорогам типа B"

Таким образом, в неоптимальной карте точно есть 2 города i, j (без ограничения общности i < j), что между ними есть
по крайней мере 2 маршрута типа R и B. Получается, что когда мы инвертируем R ребра,пути по B и R создадут
цикл между i и j.

Иными словами, задача сводится к:
1) Считывание входных данных, совершая реверс дуг с одним типом дорог(R или B).
В данной реализации происходит реверс всех дуг(дорог) типа R
2) Поиск циклов в орграфе методом DFS

Временная сложность:
V - число узлов = n
    E - число ребер = n(n-1)/2
    Граф инициализируется через список смежности, таким образом DFS пройдет по всем узлам и ребрам.
    Итого - O(n+n(n-1)/2) = O(n**2)

Пространственная сложность:
    Граф храним в списке смежности - O(E + V)
    Дополнительно храним цвета вершин и вершины на стеке - O(|V|) = O(n)
"""

from collections import defaultdict


# Стек, необходимый для работы DFS
class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, val):
        self.items.append(val)

    def is_empty(self):
        return len(self.items) == 0


# DFS + поиск цикла
def dfs_is_cyclic(start_vertex, d, colors):
    s = Stack()
    s.push(start_vertex)
    while not s.is_empty():
        v = s.pop()
        if colors[v-1] == 'white':
            colors[v-1] = 'gray'
            s.push(v)
            for w in d[v]:
                if colors[w-1] == 'white':
                    s.push(w)
                elif colors[w-1] == 'gray':
                    return True
        elif colors[v-1] == 'gray':
            colors[v-1] = 'black'
    return False


def is_cyclic(d, colors):
    return any(dfs_is_cyclic(i, d, colors) for i in range(1, len(d)))


def main():
    n = int(input())
    d = defaultdict(list)
    colors = ['white'] * n

    for i in range(1, n):
        for j, type_road in enumerate(input()):
            if type_road == 'B':
                d[i].append(i+j+1)
            elif type_road == 'R':
                d[i+j+1].append(i)
    print('NO' if is_cyclic(d, colors) else 'YES')


if __name__ == '__main__':
    main()
