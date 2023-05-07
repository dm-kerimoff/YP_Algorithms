LOCAL = False
if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    def get_node_by_index(node, index):
        while index:
            node = node.next_item
            index -= 1
        return node

    if idx == 0:
        return get_node_by_index(node, idx + 1)

    previous_node = get_node_by_index(node, idx - 1)
    if get_node_by_index(node, idx).next_item is None:
        previous_node.next_item = None
    else:
        previous_node.next_item = get_node_by_index(node, idx + 1)
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 0)
    print(new_head)


if __name__ == '__main__':
    test()
