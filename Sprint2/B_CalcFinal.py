"""
73927437 - ID посылки
ПРИНЦИП РАБОТЫ
    Для вычисления значения выражения, записанного в обратной польской нотации,
    нужно считывать выражение слева направо и придерживаться следующих шагов:
    - Обработка входного символа:
    - - Если на вход подан операнд, он помещается на вершину стека.
    - - Если на вход подан знак операции, то эта операция выполняется над требуемым количеством значений,
        взятых из стека в порядке добавления. Результат выполненной операции помещается на вершину стека.
    - Если входной набор символов обработан не полностью, перейти к шагу 1.
    - После полной обработки входного набора символов результат вычисления выражения находится в вершине стека.

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ

    Стек -- это порядок LIFO
    Наш стек поддерживает всего лишь две операции:
    - Добавить элемент в стек;
    - Извлечь элемент из стека;
    Для описания стека часто используется аббревиатура LIFO (Last In, First Out),
    подчёркивающая, что элемент, попавший в стек последним, первым будет из него извлечён.

СЛОЖНОСТЬ:
    Добавление в стек стоит O(1).
    Извлечение из стека стоит O(1).

    Стек, используемый в программе, одновременно может хранить примерно k/2 элементов,
    где k - количество цифр и операций в входной строке.
    Сложность программы O(k)
"""


class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, val):
        self.items.append(val)


def main():

    stack = Stack()
    data = input().split()
    ops = ['+', '-', '*', '/']
    for elem in data:
        if elem not in ops:
            stack.push(int(elem))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if elem == ops[0]:
                stack.push(op2 + op1)
            elif elem == ops[1]:
                stack.push(op2 - op1)
            elif elem == ops[2]:
                stack.push(op2 * op1)
            elif elem == ops[3]:
                stack.push(op2 // op1)

    print(stack.pop())


if __name__ == '__main__':
    main()