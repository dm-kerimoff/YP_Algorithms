
LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:

    def decision(root1, root2) -> bool:
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.value == root2.value:
            return decision(root1.left, root2.right) and decision(root1.right, root2.left)
        else:
            return False

    return decision(root.left, root.right)


def test():
    node1 = Node(3,  None,  None)
    node2 = Node(4,  None,  None)
    node3 = Node(4,  None,  None)
    node4 = Node(3,  None,  None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)


if __name__ == '__main__':
    test()