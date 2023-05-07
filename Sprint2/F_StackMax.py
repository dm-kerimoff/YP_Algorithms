class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_max(self):
        return None if len(self.items) == 0 else max(self.items)


stack = Stack()
n = int(input())
mas = [input() for _ in range(n)]

for elem in mas:
    if elem == 'get_max':
        print(stack.get_max())
    elif elem == 'pop':
        if len(stack.items) == 0:
            print('error')
        else:
            stack.pop()
    else:
        l = elem.split()
        stack.push(int(l[1]))
