def count_sort(n,d):
    if n > 0:
        for color in input().split(' '):
            d[color] += 1
    print('0 ' * d['0'] + '1 ' * d['1'] + '2 ' * d['2'])


def main():
    n = int(input())
    d = {'0': 0, '1': 0, '2': 0}
    count_sort(n,d)


if __name__ == '__main__':
    main()
