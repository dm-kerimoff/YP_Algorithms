def main():

    class Stack:
        def __init__(self):
            self.items = []

        def pop(self):
            self.items.pop()

        def push(self, val):
            self.items.append(val)

        def IsEmpty(self):
            return len(self.items) == 0

    def is_correct_bracket_seq(s):
        for ch in s:
            if ch == '(':
                stack.push(')')
            elif ch == '{':
                stack.push('}')
            elif ch == '[':
                stack.push(']')
            elif stack.IsEmpty() or stack.items[-1] != ch:
                return False
            else:
                stack.pop()
        return stack.IsEmpty()

    stack = Stack()
    s = input()
    print(is_correct_bracket_seq(s))


if __name__ == '__main__':
    main()

