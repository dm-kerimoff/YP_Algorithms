# 76830019
from collections import Counter, defaultdict
"""
Для каждого уникального слова из запроса берётся число его вхождений в документ, 
полученные числа для всех слов из запроса суммируются. 
Итоговая сумма и является релевантностью документа.
Чем больше сумма, тем больше документ подходит под запрос.

Идея алгоритма основана на построении поискового индекса
Отдельное спасибо коллегам по курсу за рекомендуемый ими полезный модуль collections и классы Counter, defaultkey !!!

Сложность(временная)
    n - кол-во документов;
    Создание индекса - О(n^2).
    Запрос - О(m).

Сложность(пространственная)
    Построение поискового индекса - O(n) памяти.
"""


def create_dict(files):
    """
    Для лаконичной работы со словарём использован словарь с дефолтным значением defaultkey, чтобы избежать проверок
    существования ключа и инициализации вручную несуществующих ключей
    Счётчик Counter предназначен для удобных и быстрых подсчетов количества появлений неизменяемых элементов в последовательностях,
    имеет интерфейс словаря
    Результат функции - словарь  формата:
    {word1:{doc1: count, doc2: count,...,}, word2: {doc2: count,...}, wordN: {doc1: count},...,  }
    """
    word_dict = defaultdict(dict)
    for filename, words in enumerate(files):
        for word, cnt in Counter(words).items():
            word_dict[word][filename] = cnt
    return word_dict


def search_query(d_word, string, count_docs, lim=5):
    """
    Сортировка документов на выдаче производится по убыванию релевантности.
    Если релевантности документов совпадают, то по возрастанию их порядковых номеров в базе (то есть во входных данных).
    """
    result = [[0, i] for i in range(count_docs)]
    for word in set(string.split()):
        if word in d_word.keys():
            for filename, cnt in d_word[word].items():
                result[filename][0] -= cnt
    # Возвращаем индексы самых релевантных документов по убыванию
    return [index for cnt, index in sorted([(cnt, index) for cnt, index in result if cnt < 0])[:lim]]


def main():
    n = int(input())
    documents = [[]] + [input().split() for _ in range(n)]
    d_word = create_dict(documents)
    m = int(input())
    for _ in range(m):
        print(*search_query(d_word, input(), n+1, lim=5))


if __name__=='__main__':
    main()
