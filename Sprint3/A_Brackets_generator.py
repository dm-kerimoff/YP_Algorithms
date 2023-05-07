def is_correct(s):
    for _ in range(len(s) // 2):
        s = s.replace('()', '')
    return len(s) == 0


def gen_binary(n, f=''):
    if n == 0 and is_correct(f):
        print(f)
    elif n != 0:
        gen_binary(n - 1, f'{f}(')
        gen_binary(n - 1, f'{f})')


def main():
    n = int(input())
    gen_binary(n * 2)


if __name__ == '__main__':
    main()