"""
id посылки - 86729032

Этапы решения задачи:
 а) Построение бора - префиксного дерева, в терминальных узлах которого расположена длина слова
 б) Построение булевого динамического массива dp[i] - возможность создания строки с индексом i
 Ответ на вопрос задачи - это dp[-1]

Подробные разъяснения:

Мы идём по строке и отмечаем все места до куда можно дойти с текущими словами и проверяем, можно ли дойти до конца этой строки
Базовый динамический массив dp - всё значения False и во все места, куда мы можем дойти, ставим true

!!! В терминальном узле запишем вспомогательную информацию - длину слова
Длина слова в узле в данном случае играет роль индикатора, является символ терминальным или нет, то есть заканчивается
им какое-либо слово или нет.
По умолчанию - символ нетерминальный |-> self.terminal = False
Если символ терминальный, значит этим символом заканчивается какое-то слово из бора |-> self.terminal = длина слова
После терминального слова могут идти другие узлы
В self.terminal в терминальный узел можно вписывать True вместо длины слова, т.к на решение данной задачи это не повлияет.
Для других задач, возможно, эта информация была бы полезной и необходимой
!!!
Временная сложность:
    Построение бора: O(L), где L — суммарная длина слов во множестве
    Проход по дереву - O(n^2), где n - длина текста

Пространственная сложность:
    Бор: O(L), где L — суммарная длина слов во множестве
    Текст: O(n), где n - длина текста

Наработки и логика работы функции is_split_text были позаимствованы в интернете
"""


class TrieNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = {} if children is None else children
        self.terminal = False


def bor_create(words):  # Функция построения префиксного дерева с возвращением корня бора
    root = TrieNode('')
    for word in words:
        node = root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.terminal = len(word)       # Пометим терминальый узел длиной слова

    return root


def is_split_text(text, words):
    root = bor_create(words)        # Бор с корнем root создан и готов к использованию
    dp = [True] + [False] * len(text)   # Булевый динамический массив
    for i in range(len(text)):
        node = root
        if dp[i]:
            for j in range(i, len(text) + 1):
                if node.terminal:   # Если узел терминальный и он последний -> в строке найдено слово из бора
                    dp[j] = True
                if j == len(text) or not node.children.get(text[j], False):
                    break
                node = node.children[text[j]]
    return dp[-1]


def main():
    text = input()  # Данный текст
    words = [input() for _ in range(int(input()))]  # список допустимых к использованию слов
    print('YES' if is_split_text(text, words) else 'NO')


if __name__ == "__main__":
    main()
