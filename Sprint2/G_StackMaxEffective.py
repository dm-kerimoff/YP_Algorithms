class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        self.items.pop()

    def push(self, val):
        if len(self.items) == 0:
            self.items.append(val)
        else:
            self.items.append(max(val, self.items[-1]))

    def get_max(self):
        return None if len(self.items) == 0 else self.items[-1]


highs = Stack()
n = int(input())
for _ in range(n):
    elem = input()
    if elem == 'get_max':
        print(highs.get_max())
    elif elem == 'pop':
        if len(highs.items) == 0:
            print('error')
        else:
            highs.pop()
    else:
        l = elem.split()
        highs.push(int(l[1]))

