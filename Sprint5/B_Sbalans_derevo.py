LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    def DFS(root):
        if root is None:
            return 0

        LeftSubtreeHeight = DFS(root.left)

        if LeftSubtreeHeight == -1:
            return -1
        
        RightSubtreeHeight = DFS(root.right)
        if RightSubtreeHeight == -1:
            return -1

        if abs(LeftSubtreeHeight - RightSubtreeHeight) > 1:
            return -1
        return max(LeftSubtreeHeight, RightSubtreeHeight) + 1

    return DFS(root) != -1


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()