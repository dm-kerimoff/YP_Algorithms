class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = {} if next is None else next
        self.terminal = False


def bor_create(words):  # Функция построения префиксного дерева с возвращением корня бора
    root = Node('')
    for word in words:
        node = root

        for char in word:
            node.next[char] = node.next.get(char, Node(char))
            node = node.next[char]
        node.terminal = len(word)       # Длина слова записана в терминальном узле

    return root


def main():
    #text = input()  # Данный текст
    words = [input() for _ in range(int(input()))]  # список допустимых к использованию слов
    print(bor_create(words))


if __name__ == "__main__":
    main()
