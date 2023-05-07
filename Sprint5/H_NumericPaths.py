LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root, val=0) -> int:
    val = val * 10 + root.value
    summ = 0

    if root.left is not None:
        summ += solution(root.left, val)

    if root.right is not None:
        summ += solution(root.right, val)

    if summ == 0:
        summ = val

    return summ


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275


if __name__ == '__main__':
    test()