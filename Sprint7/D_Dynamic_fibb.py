def main():
    n = int(input())
    l = 1
    r = 1
    for _ in range(n):
        l,r = r,l
        r = (l + r) % 1000000007
    print(l)


if __name__ == '__main__':
    main()

