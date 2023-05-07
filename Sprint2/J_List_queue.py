def main():

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    class ListQueue:
        def __init__(self, value=None, next=None):
            self.size = 0
            self.head = None
            self.tail = None

        def is_empty(self):
            return self.size == 0

        def get(self):
            res = self.head.value
            self.head = self.head.next
            self.size -= 1
            return res

        def put(self, x):
            N = Node(x)
            if self.size == 0:
                self.head = N
                self.tail = N
            else:
                self.tail.next = N
                self.tail = N
            self.size += 1

    n = int(input())    #количество команд
    q = ListQueue()
    for _ in range(n):
        elem = input()
        if elem == 'get':
            if q.is_empty():
                print('error')
            else:
                print(q.get())
        elif elem == 'size':
            print(q.size)
        else:
            l = elem.split()
            q.put(int(l[1]))


if __name__ == '__main__':
    main()
