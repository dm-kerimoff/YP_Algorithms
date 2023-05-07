"""
Успешная посылка: 82832728
В данной реализации использовалась приоритетная очередь - куча(max-heap) c использованием модуля heapq

Временная сложность:
Мы используем кучу(max-heap) -> О(logV) времени
В общем случае:
O(E*logV), где E - количество рёбер в графе, а V - количество вершин.

Пространственная сложность:
    Хранение кучи - O(n).
    Список смежности - O(E+V), где E - количество вершин, V - количество рёбер.
    В матрице будет V  ключей, а значений в сумме 2E (каждое ребро хранится по два раза так как граф неориентированный).
"""
import heapq


# Функция добавления вершины в остов
def add_vertex(v, added, not_added, graph_edges, edges):
    added.add(v)
    not_added.remove(v)
    for edge, weight in graph_edges:
        if edge in not_added:
            heapq.heappush(edges, (-weight, edge))  # Добавление всех инцидентных рёбер, сохраняя максимальность кучи


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    max_span_sum = 0
    added = set()  # Множество вершин, уже добавленных в остов.
    not_added = set(range(1, n+1))  # Множество вершин, ещё не добавленных в остов.
    edges = []  # Массив рёбер, исходящих из остовного дерева.

    for _ in range(m):
        f, t, w = map(int, input().split())
        graph[f].append([t, w])
        graph[t].append([f, w])

    add_vertex(1, added, not_added, graph[1], edges)

    while not_added and edges:
        weight, vertex = heapq.heappop(edges)
        if vertex in not_added:
            max_span_sum += abs(weight)
            add_vertex(vertex, added, not_added, graph[vertex], edges)

    print('Oops! I did it again' if not_added else max_span_sum)


if __name__ == '__main__':
    main()
