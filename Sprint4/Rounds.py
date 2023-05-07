def main():
    n = int(input())
    d = {}
    for _ in range(n):
        elem = input()
        if elem not in d:
            d[elem] = 1
        else:
            d[elem] += 1
    for key in d:
        if d[key] != 0:
            print(key)


if __name__ == '__main__':
    main()