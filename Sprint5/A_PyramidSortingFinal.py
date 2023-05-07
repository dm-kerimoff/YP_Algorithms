"""
id посылки: 80383139
Сложность удаления узла составляет O(h), где h - высота дерева
Для стека вызовов(рекурсии) требуется пространство O(h)
Комментарии к решению приведены
"""


class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def remove(root, key):
    # Базовый случай: ключ не найден в дереве
    if root is None:
        return root
    if key < root.value:        # если данный ключ меньше корневого узла, повторить для левого поддерева
        root.left = remove(root.left, key)
    elif key > root.value:      # если данный ключ больше, чем корневой узел, повторить для правого поддерева
        root.right = remove(root.right, key)
    elif root.left is None and root.right is None:  # Случай 1: удаляемый узел не имеет потомков (это конечный узел)
        # обновить корень до None
        return None
    elif root.left and root.right:                  # Случай 2: удаляемый узел имеет двух потомков
        # Находит свой неупорядоченный узел-потомок
        max_key = find_maximum_key(root.left)
        # копирует значение потомка в текущий узел
        root.value = max_key.value
        # Рекурсивное удаление потомка
        root.left = remove(root.left, max_key.value)
    else:                                           # Случай 3: удаляемый узел имеет только одного потомка
        # выбирает дочерний узел
        child = root.left or root.right
        root = child
    return root


# Функция для поиска узла максимального значения в поддереве с корнем node
def find_maximum_key(node):
    while node.right:
        node = node.right
    return node


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8


if __name__ == '__main__':
    test()
